import random

# 26 lowercase letters
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
# 26 uppercase letters
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 13 special characters
SPECIAL = "~!@#$%^&*()_+"
# 10 digits
NUMBER = "1234567890"
ALL_CHARS = LOWERCASE + UPPERCASE + SPECIAL + NUMBER


def generatePassword(length) -> str:
    if length < 12:
        length = 12

    password = []
    password.append(LOWERCASE[random.randint(0, 25)])
    password.append(UPPERCASE[random.randint(0, 25)])
    password.append(SPECIAL[random.randint(0, 12)])
    password.append(NUMBER[random.randint(0, 9)])

    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0, 74)])

    random.shuffle(password)
    return "".join(password)





