# my solution
def reverse_string(string):
    return string[::-1]

# suggested solution requirements: list(), for loops, range(), len(), integer division, indexes, swapping values, join()
def reverseString(text):
    text = list(text)
    for i in range(len(text) // 2):
        mirrorIndex = len(text) - i - 1
        text[i], text[mirrorIndex] = text[mirrorIndex], text[i]
    return "".join(text)
