def space(n):

    num = 0
    temp = n
    while temp > 0:
        temp //= 10
        num += 1

    for i in range(num - 1, -1):
        div = 10**i
        dig = n // div
        print(dig, end=" ")
        n %= div


space(12345)


# print(12345 // 10000) 1
# print(2345 // 1000) 2
# print(345 // 100) 3
# print(45 // 10) 4
# print(5 // 1) 5
