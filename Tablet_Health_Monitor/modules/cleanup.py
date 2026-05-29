from core.logger import log
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy as By


def cleanup(serial):
    log("CLEANUP", "Opening Recent Apps")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = serial
    options.no_reset = True

    driver = webdriver.Remote("http://localhost:4723", options=options)

    try:
        driver.press_keycode(187)  # Recent apps
        time.sleep(2)

        clear_all = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@text='Close all' or @text='Clear all']"))
        )
        clear_all.click()

        log("CLEANUP", "Recent apps cleared")

    except Exception as e:
        log("CLEANUP", f"No recent apps to clear: {e}")

    finally:
        driver.quit()
