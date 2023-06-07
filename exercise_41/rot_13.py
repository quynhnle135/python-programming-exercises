def rot_13(text):
    encryptedText = ""
    for character in text:
        if not character.isalpha():
            encryptedText += character
        else:
            rotatedLetterOrdinal = ord(character) + 13
            if character.islower() and rotatedLetterOrdinal > 90:
                rotatedLetterOrdinal -= 26
            if character.isupper() and rotatedLetterOrdinal > 90:
                rotatedLetterOrdinal -= 26

            encryptedText += chr(rotatedLetterOrdinal)
    return encryptedText
