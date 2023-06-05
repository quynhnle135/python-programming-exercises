def convert_int_to_str(number):
    if number == 0:
        return '0'
    result = ""
    DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    is_negative = False
    if number < 0:
        is_negative = True
        number = -number

    while number > 0:
        digit = number % 10
        number //= 10
        result = DIGITS_INT_TO_STR[digit] + result

    if is_negative:
        result = "-" + result

    return result