import subprocess

def collect_health(serial):
    battery = subprocess.check_output(f"adb -s {serial} shell dumpsys battery", shell=True).decode()
    storage = subprocess.check_output(f"adb -s {serial} shell df /data", shell=True).decode()
    return {"battery": battery, "storage": storage}
