from core.detect_device import detect_device
from core.unlock_device import unlock_device
from modules.collect_health import collect_health
from modules.get_os_info import get_os_info
from modules.get_app_versions import get_app_versions
from modules.hub_enrollment import hub_enrollment
from modules.screenshot import capture_screenshot
from modules.export_excel import export_excel
from modules.update_word import update_word
from modules.cleanup import cleanup
from core.logger import log

   
def run_health_monitor():
    log("INIT", "Starting Tablet Health Monitor")

    serial = detect_device()
    unlock_device(serial)

    info = get_os_info(serial)

    # HUB ENROLLMENT (NEW FAST MODULE)
    hub = hub_enrollment(serial)

    info["uat"] = hub["uat"]
    info["group_id"] = hub["group"]
    info["username"] = hub["username"]

    # Continue pipeline
    info["apps"] = get_app_versions(serial)
    screenshot(serial)
    export_excel(info)
    update_word(info)

    cleanup(serial)

    log("RESULT", "Pipeline completed successfully")

