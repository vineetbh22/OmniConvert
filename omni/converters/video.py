import subprocess
import os
import logging

logging.basicConfig(level=logging.INFO)


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

    if options.get("resolution"):
        cmd += ["-s", options["resolution"]]

    if options.get("preset"):
        cmd += ["-preset", options["preset"]]

    cmd.append(output_file)

    try:
        subprocess.run(cmd, check=True)
        logging.info("✅ Converted: %s → %s", input_file, output_file)
        # print(f"✅ Converted: {input_file} → {output_file}")
    except subprocess.CalledProcessError as e:
        logging.error("❌ Conversion failed")
        raise e