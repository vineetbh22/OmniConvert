# omni\utils\log_tracker.py
from datetime import datetime
import json
import os

os.makedirs("logs", exist_ok=True)


def _track_log(input_file: str,output_file : str,file_size_bytes: int, 
               resolution: str, bitrate: float, duration: int, options: dict = None):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input": input_file,
        "output": output_file,
        "size": file_size_bytes,
        "resolution": resolution,
        "bitrate": bitrate,
        "time_taken_sec": duration,
        "options": options
    }

    with open("logs/conversion_log.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")