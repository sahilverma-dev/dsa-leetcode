n = 5


for i in range(1, n + 1):
    str = ""
    for j in range(n - i):
        str += " "
    for k in range(i - 1):
        str += "* "
    print(str)
