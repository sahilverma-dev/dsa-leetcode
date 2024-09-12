# 1588. Sum of All Odd Length Subarraysa


def sumOddLengthSubarrays(arr):
    total = 0
    n = len(arr)

    for i in range(n):
        for j in range(i, n):

            if (j - i + 1) % 2 == 1:
                total += sum(arr[i : j + 1])

    return total
