# omni\core\dispatcher.py
import os
from omni.converters.video import convert_video

VIDEO_FORMATS = {"mp4", "avi", "mkv", "mov", "webm"}

def dispatch(input_file: str, output_file: str, options: dict):
    input_ext = os.path.splitext(input_file)[1][1:].lower()
    output_ext = os.path.splitext(output_file)[1][1:].lower()

    if input_ext in VIDEO_FORMATS and output_ext in VIDEO_FORMATS:
        return convert_video(input_file, output_file, options)

    raise ValueError(f"Unsupported conversion: {input_ext} → {output_ext}")