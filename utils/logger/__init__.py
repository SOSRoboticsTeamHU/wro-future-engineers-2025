import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
log_file_path = os.path.join(LOG_DIR, f"robot_{timestamp}.log")

def log(message):
    time_tag = datetime.now().strftime("%H:%M:%S")
    full_message = (
        f"[{time_tag}] {message}"
    )
    print(full_message)

    with open(log_file_path, "a") as log_file:
        log_file.write(full_message + "\n")
