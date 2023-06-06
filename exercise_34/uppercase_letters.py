def get_upper_case(text):
    LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
                      'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
                      'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

    uppercase_text = ""
    for t in text:
        if t in LOWER_TO_UPPER:
            uppercase_text += LOWER_TO_UPPER[t]
        else:
            uppercase_text += t

    return uppercase_text