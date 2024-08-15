n = 4


for i in range(n + 1):
    str = ""
    for j in range(n):
        if j < n - i:
            str += " "
        else:
            str += " *"

    print(str)


for i in range(n + 1):
    str = ""

    for j in range((i)):
        str += " "
    for j in range((n - i + 1)):
        str += "* "

    print(str)
