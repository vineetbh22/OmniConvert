# omni\converters\video.py
from tqdm import tqdm
import subprocess
import os
import logging
import shutil
import time
import json
from omni.utils.format_size import _format_size
from omni.utils.format_time import _format_time
from omni.utils.log_tracker import _track_log

logging.basicConfig(level=logging.INFO)


if not shutil.which("ffmpeg"):
    raise Exception("❌ FFmpeg not found. Please install and add to PATH.")


def get_duration(input_file):
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        input_file,
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return float(result.stdout)


def get_video_metadata(file_path):
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,bit_rate",
        "-of",
        "json",
        file_path,
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    data = json.loads(result.stdout)

    stream = data["streams"][0]
    bitrate = stream.get("bit_rate")
    bitrate = int(bitrate) // 1000 if bitrate else 0  # kbps

    return {
        "resolution": f"{stream.get('width')}x{stream.get('height')}",
        "bitrate": bitrate,
    }


def convert_video(input_file: str, output_file: str, options: dict = None):
    if options is None:
        options = {}

    cmd = ["ffmpeg", "-y", "-i", input_file]

    # Optional flags
    if options.get("copy"):
        cmd += ["-c", "copy"]  # no re-encoding (fast)

    elif options.get("codec"):
        cmd += ["-c:v", options["codec"]]

    else:
        cmd += ["-c:v", "libx264", "-c:a", "aac"]

    if options.get("compatibility") == "windows":
        cmd += ["-pix_fmt", "yuv420p"]

    if options.get("resolution"):
        cmd += ["-s", options["resolution"]]

    if options.get("preset"):
        cmd += ["-preset", options["preset"]]

    # progress pipe for stdout
    # cmd += ["-progress", "pipe:1", "-nostats"]

    cmd.append(output_file)

    try:
        # sync runs
        # raise exception with check
        # subprocess.run(cmd, check=True)
        # capture normal output in stdout and errors/logs in stderr
        # result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        start_time = time.time()
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,  # STDOUT,   # 🔥 merge streams
            text=True,
            bufsize=1,
            # universal_newlines=True
        )
        tqdm.write("\n🎬 Converting:\n")

        total_duration = get_duration(input_file)

        # tracking vars
        current_time = 0
        frame = 0
        speed = "0x"

        # % progress bar        cyan
        with tqdm(total=100, desc="🎬 Converting", unit="%", colour="#00b3b3") as pbar:
            last_progress = 0
            for line in process.stderr:
                line = line.strip()

                if not line:
                    break

                # parse ffmpeg progress output
                if "time=" in line:
                    try:
                        # extract time=00:01:23.45
                        time_str = line.split("time=")[1].split(" ")[0]

                        h, m, s = time_str.split(":")
                        current_time = float(h) * 3600 + float(m) * 60 + float(s)

                        progress = (current_time / total_duration) * 100

                        delta = progress - last_progress
                        if delta > 0:
                            pbar.update(delta)
                            last_progress = progress

                    except Exception:
                        pass

                if "frame=" in line:
                    try:
                        frame = int(line.split("frame=")[1].split()[0])
                    except Exception:
                        frame = 0

                if "speed=" in line:
                    try:
                        speed = line.split("speed=")[1].split()[0]
                    except Exception:
                        speed = "0x"

                s_value = float(speed.rstrip("x")) if speed.strip() != "N/A" else 0.0
                eta = (total_duration - current_time) / s_value if s_value > 0 else 0
                eta_str = time.strftime("%H:%M:%S", time.gmtime(eta))

                # update description (live info)
                pbar.set_description(f"🎞️ Frame: {frame}s |⚡Speed: {speed}")
                # update postfix (live info)
                pbar.set_postfix(
                    {
                        "⏱ Time": f"{current_time:.1f}s/{total_duration:.1f}s",
                        # "🎞️frame": frame,
                        # "⚡ speed": speed,
                        "⏳ETA": eta_str,
                    }
                )

        process.wait()

        end_time = time.time()
        duration = end_time - start_time

        if process.returncode != 0:
            stderr_output = process.stderr.read()
            stdout_output = process.stdout.read()
            logging.error("stderr: %s\nstdout: %s", stderr_output, stdout_output)
            raise Exception("❌ FFmpeg failed")

        metadata = get_video_metadata(output_file)
        file_size_bytes = os.path.getsize(output_file)

        tqdm.write("\n🎉 Conversion Complete!")
        print(f"📁 File: {output_file}")
        print(f"📦 Size: {_format_size(file_size_bytes)}")
        print(f"🎥 Resolution: {metadata['resolution']}")
        print(f"⚡ Bitrate: {metadata['bitrate']} kbps")
        print(f"⏳ Time Taken: {_format_time(duration)}")

        logging.info(
            "✅ Converted: %s → %s \n %s\t%s",
            input_file,
            output_file,
            _format_size(file_size_bytes),
            _format_time(duration),
        )

    except subprocess.CalledProcessError as e:
        logging.error("❌ Conversion failed")
        raise e
    finally:
        if "file_size_bytes" in locals() and "metadata" in locals():
            _track_log(
                input_file,
                output_file,
                file_size_bytes,
                metadata["resolution"],
                metadata["bitrate"],
                duration,
                options,
            )
