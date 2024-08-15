def flip_cases(str):
    newStr = ""
    for c in str:
        ordinate = ord(c)
        if ordinate >= 65 and ordinate <= 90:
            newStr += chr(ord(c) + (97 - 65))
        elif ordinate >= 97 and ordinate <= 122:
            newStr += chr(ord(c) - (97 - 65))
    return newStr


# 65 - 90
# 97 - 122

print(flip_cases("AbCdE"))
print(flip_cases("aBcDe"))
