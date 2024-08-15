n = 5


for i in range(1, n + 1):
    str = ""

    for j in range(i):
        str += " "
    for j in range(n):
        str += " *"

    print(str)
