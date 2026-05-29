from core.adb_utils import is_locked, unlock

def unlock_device(serial):
    if is_locked(serial):
        unlock(serial)
