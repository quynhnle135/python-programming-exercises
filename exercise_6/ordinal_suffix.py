# my solution
def ordinal_suffix(number) -> str:
    copy_number = number
    if number in [11, 12, 13]:
        return str(number) + "th"

    last_digit = copy_number % 10
    result = ""

    if last_digit == 1:
        result = str(number) + "st"
    elif last_digit == 2:
        result = str(number) + "nd"
    elif last_digit == 3:
        result = str(number) + "rd"
    else:
        result = str(number) + "th"

    return result

# suggested solution
def ordinal_suffix_optimal(number) -> str:
    numberStr = str(number)
    # check if the last two digit is 11, 12, or 13
    if numberStr[-2:] in ("11", "12", "13"):
        return numberStr + "th"

    if numberStr[-1:] == "1":
        return numberStr + "st"
    elif numberStr[-1] == "2":
        return numberStr + "nd"
    elif numberStr[-1] == "3":
        return numberStr + "rd"
    else:
        return numberStr + "th"