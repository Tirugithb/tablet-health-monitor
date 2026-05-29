from tablet_health_monitor import run_health_monitor
from core.start_appium import start_appium

start_appium()   # Auto-launch Appium

if __name__ == "__main__":
    run_health_monitor()
