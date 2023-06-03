def validate_date(year, month, day):
    if year < 0:
        return False
    if month <= 0 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day <= 0 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day <= 0 or day > 30:
            return False
    if month == 2 and is_leap_year(year):
        if day > 29:
            return False
    elif month == 2 and not is_leap_year(year):
        if day > 28:
            return False
    return True

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False