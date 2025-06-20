#!/usr/bin/env python3

import subprocess
import time


MINUTES = 9
WORKSPACE = 2
QUALITY = 88
OFFSET = "1920x1200+1920+0"
DIR = "/home/yo/tres_images"
EXT = "png"


def get_seconds():
    return int(time.time())


def restore():
    subprocess.call(["wmctrl", "-s", "0"])


def screenshot():
    try:
        # Switch to the third workspace (index 2)
        subprocess.call(["wmctrl", "-s", str(WORKSPACE)])

        # Brief pause to ensure the switch completes
        time.sleep(0.5)
        filename = f"{DIR}/{get_seconds()}.{EXT}"

        subprocess.run([
            "maim",
            "-g",
            OFFSET,
            "-o",
            filename,
        ])

        print(f"Saved: {filename}")

        # Switch back to the original workspace
        time.sleep(0.2)
        restore()

    except Exception as e:
        print(f"Error capturing workspace: {e}")

        # Ensure we try to return to the original workspace even if an error occurs
        try:
            restore()
        except:
            pass


def screenshot_loop():
    try:
        print("Starting screenshot loop...")

        while True:
            screenshot()
            time.sleep(60 * MINUTES)
    except KeyboardInterrupt:
        print("Workspace capture loop stopped by user")


if __name__ == "__main__":
    screenshot_loop()