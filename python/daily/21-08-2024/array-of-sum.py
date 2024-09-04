from typing import List


def sumOfArray(arr: List, i: int = 0) -> int:
    if i == len(arr):
        return 0
    else:
        return arr[i] + sumOfArray(arr, i + 1)


print(sumOfArray([1, 2, 3, 4, 5]))  # 15
