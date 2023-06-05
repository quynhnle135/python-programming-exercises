def convert_str_to_int(string):
    if string == '0':
        return 0
    is_negative = False
    if string[0] == "-":
        is_negative = True
        string = string[1:]
    STR_TO_DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    result = 0
    while string:
        digit = string[0]
        string = string[1:]
        result = result * 10 + STR_TO_DIGITS[digit]

    if is_negative:
        result = -result
    return result
