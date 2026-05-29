import subprocess
import time
import socket
from core.logger import log

def is_appium_running(host="127.0.0.1", port=4723):
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except:
        return False


def start_appium():
    if is_appium_running():
        log("APPIUM", "Appium already running")
        return

    log("APPIUM", "Starting Appium Server...")

    subprocess.Popen(
        "appium --port 4723",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(5)
    log("APPIUM", "Appium started")
