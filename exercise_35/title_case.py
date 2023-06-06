def get_title_case(text):
    title_text = ""
    for i in range(len(text)):
        if i == 0:
            title_text += text[i].upper()
        elif text[i].isalpha() and not text[i - 1].isalpha():
            title_text += text[i].upper()
        else:
            title_text += text[i].lower()
    return title_text