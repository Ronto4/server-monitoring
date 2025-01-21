from typing import Optional
import psutil


def check(
    *,
    min_level: Optional[float] = None,
    max_level: Optional[float] = None,
    is_charging: Optional[bool] = None
) -> bool:
    battery = psutil.sensors_battery()
    if battery is None:
        return False
    battery_level = battery.percent
    charger_plugged_in = battery.power_plugged
    if is_charging is not None and is_charging != charger_plugged_in:
        return False
    if min_level is not None and battery_level < min_level:
        return False
    if max_level is not None and battery_level > max_level:
        return False
    return True
