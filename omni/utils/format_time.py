# omni\utils\format_time.py
def _format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{int(mins)}m {int(secs)}s"


if __name__ == "__main__":
    secs = int(input("Enter the seconds\t"))
    print(_format_time(secs))
