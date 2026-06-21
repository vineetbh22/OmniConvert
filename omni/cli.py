# omni\cli.py
import argparse
from omni.core.dispatcher import dispatch


def main():
    parser = argparse.ArgumentParser(description="OmniConvert CLI")

    parser.add_argument("input", help="Input file")
    parser.add_argument("output", help="Output file")

    parser.add_argument(
        "--copy", action="store_true", help="Stream copy (no re-encoding)"
    )
    parser.add_argument("--codec", help="Video codec (e.g., libx264)")
    parser.add_argument("--compatibility", help="e.g. windows")
    parser.add_argument("--resolution", help="e.g. 1280x720")
    parser.add_argument("--preset", help="ffmpeg preset (fast, slow, etc)")
    parser.add_argument("--quality", type=int, default=85, help="Quality for images (1-100)")
    parser.add_argument("--enhance", action="store_true", help="Smart image enhancement (contrast, sharpness)")

    args = parser.parse_args()

    options = {
        "copy": args.copy,
        "codec": args.codec,
        "compatibility": args.compatibility,
        "resolution": args.resolution,
        "preset": args.preset,
        "quality": args.quality,
        "enhance": args.enhance,
    }

    dispatch(args.input, args.output, options)


if __name__ == "__main__":
    main()
