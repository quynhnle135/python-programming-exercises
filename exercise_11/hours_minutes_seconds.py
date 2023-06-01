def get_hours_minutes_seconds(total_seconds) -> str:
    if total_seconds == 0:
        return "0s"

    hours = 0
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        total_seconds %= 3600

    minutes = 0
    if total_seconds >= 60:
        minutes = total_seconds // 60
        total_seconds %= 60

    seconds = total_seconds
    hms = []

    if hours > 0:
        hms.append(str(hours) + "h")

    if minutes > 0:
        hms.append(str(minutes) + "m")

    if seconds > 0:
        hms.append(str(seconds) + "s")

    return " ".join(hms)

