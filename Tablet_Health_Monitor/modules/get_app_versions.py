import subprocess

def get_app_versions(serial):
    output = subprocess.check_output(f"adb -s {serial} shell pm list packages -f", shell=True).decode()
    apps = {}

    for line in output.splitlines():
        pkg = line.split("=")[-1]
        version = subprocess.check_output(
            f"adb -s {serial} shell dumpsys package {pkg} | grep versionName",
            shell=True
        ).decode(errors="ignore").strip()

        apps[pkg] = version.replace("versionName=", "")

    return apps
