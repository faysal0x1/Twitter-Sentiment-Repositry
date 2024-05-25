import os
import datetime
import time  # Importing time module


def pause_download():
    os.system("idman /s")
    print("Download paused.")
    time.sleep(30)  # Pause execution for 30 seconds


def start_download():
    os.system("idman /d")
    print("Download started.")


# Example logic to pause download during certain hours
def main():
    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour < 8:  # Pause download between midnight and 8 AM
        pause_download()
        start_download()  # Resume download after 30 seconds
    else:
        start_download()


if __name__ == "__main__":
    main()
