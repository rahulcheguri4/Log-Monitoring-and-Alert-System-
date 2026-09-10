import re
import time
import logging


# -------------------------------
# Configuration
# -------------------------------

LOG_FILE = "app.log"
ALERT_FILE = "alerts.log"

ERROR_THRESHOLD = 2

CHECK_INTERVAL = 5


# -------------------------------
# Logging configuration
# -------------------------------

logging.basicConfig(
    filename=ALERT_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------------------
# Error pattern
# -------------------------------

ERROR_PATTERN = re.compile(r"\bERROR\b", re.IGNORECASE)


# -------------------------------
# Send Alert
# -------------------------------

def send_alert(error_count):
    message = (
        f"ALERT: Error threshold crossed! "
        f"Total errors detected: {error_count}"
    )

    print(message)

    logging.warning(message)


# -------------------------------
# Monitor log file
# -------------------------------

def monitor_log():

    print("Log monitoring started...")
    print("Press CTRL+C to stop.")

    error_count = 0

    with open(LOG_FILE, "r") as file:

        # Move to end of file
        file.seek(0, 2)

        while True:

            line = file.readline()

            if not line:
                time.sleep(CHECK_INTERVAL)
                continue

            # Check ERROR pattern
            if ERROR_PATTERN.search(line):

                error_count += 1

                print("Error detected:")
                print(line.strip())

                if error_count >= ERROR_THRESHOLD:
                    send_alert(error_count)

                    # Reset counter after alert
                    error_count = 0


# -------------------------------
# Main program
# -------------------------------

if __name__ == "__main__":

    try:
        monitor_log()

    except FileNotFoundError:

        print("Error: app.log file not found.")

    except KeyboardInterrupt:

        print("\nLog monitoring stopped.")