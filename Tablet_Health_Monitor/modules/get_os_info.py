import subprocess

def get_os_info(serial):
    model = subprocess.check_output(f"adb -s {serial} shell getprop ro.product.model", shell=True).decode().strip()
    android = subprocess.check_output(f"adb -s {serial} shell getprop ro.build.version.release", shell=True).decode().strip()
    patch = subprocess.check_output(f"adb -s {serial} shell getprop ro.build.version.security_patch", shell=True).decode().strip()

    return {"model": model, "android": android, "patch": patch}
