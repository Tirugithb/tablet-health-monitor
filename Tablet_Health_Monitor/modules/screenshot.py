import subprocess

def capture_screenshot(serial):
    path = "C:/Temp/software_info.png"
    subprocess.run(f"adb -s {serial} exec-out screencap -p > {path}", shell=True)
    return path
