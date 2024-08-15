n = 5


for i in range(1, n + 1):
    str = ""
    for j in range(n):
        if j < n - i:
            str += "  "
        else:
            str += " *"

    print(str)


# for i in range(1, n + 1):
#     str = ""
#     for j in range(1, n + 1):
#         if j <= i:
#             str += "  "
#         else:
#             str += " *"
#     print(str)
