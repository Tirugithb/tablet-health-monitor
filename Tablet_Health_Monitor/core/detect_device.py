import subprocess

def detect_device():
    out = subprocess.check_output("adb devices", shell=True).decode()
    for line in out.splitlines():
        if "\tdevice" in line:
            return line.split()[0]
    raise RuntimeError("No device detected")
