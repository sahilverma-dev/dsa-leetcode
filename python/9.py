n = 5


for i in range(n):
    str = ""

    for j in range(i):
        str += " "

    for j in range(n - i):
        if j == 0:
            str += "*"
        else:
            str += " *"

    print(str)


for i in range(2, n + 1):
    str = ""

    for j in range(n - i):
        str += " "

    for j in range(i):
        if j == 0:
            str += "*"
        else:
            str += " *"

    print(str)
