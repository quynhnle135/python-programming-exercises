# using replace() and find() functions in python
def find_and_replace(str_input, old_text, new_text) -> str:
    if str_input.find(old_text) >= 0:
        return str_input.replace(old_text, new_text)
    else:
        return str_input


def find_and_replace_advanced(str_input, old_text, new_text) -> str:
    i = 0
    replaced_text = ""
    while i < len(str_input):
        if str_input[i:i + len(old_text)] == old_text:
            replaced_text += new_text
            i += len(old_text)
        else:
            replaced_text += str_input[i]
            i += 1
    return replaced_text

