import subprocess

PASSWORD = "Medtronic1"

def is_locked(serial):
    state = subprocess.check_output(f"adb -s {serial} shell dumpsys window", shell=True).decode()
    return "mDreamingLockscreen=true" in state

def unlock(serial):
    subprocess.run(f"adb -s {serial} shell input text {PASSWORD}", shell=True)
    subprocess.run(f"adb -s {serial} shell input keyevent 66", shell=True)
