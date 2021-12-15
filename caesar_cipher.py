def encrypt(text2, s):
    result = ""
    for i in range(len(text2)):
        char = text2[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result


def decrypt(text1, s):
    result = ""
    for i in range(len(text1)):
        char = text1[i]
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
