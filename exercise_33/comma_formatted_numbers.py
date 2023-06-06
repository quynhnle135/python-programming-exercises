def format_numbers(number):
    # convert number to a string
    number = str(number)

    # remember the fractional part and remove it from the number, if any
    if "." in number:
        fractional_part = number[number.index("."):]
        number = number[:number.index(".")]
    else:
        fractional_part = ""

    triplet = ""
    comma_number = ""
    # getting number from tail to  head
    for i in range(len(number) - 1, -1, -1):
        triplet = number[i] + triplet
        if len(triplet) == 3:
            comma_number = triplet + "," + comma_number
            triplet = ""

    if triplet != "":
        comma_number = triplet + "," + comma_number

    return comma_number[:-1] + fractional_part
