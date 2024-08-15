from typing import List


def secondLargestElement(arr: List):
    # brute force
    # sort the list and return second last element
    # return sorted(arr)[-2]

    # without sorting

    second_max = float("-inf")
    n = len(arr)
    for i in range(n):
        # print(second_max)
        if i == n - 1:
            return min(second_max, arr[i])
        else:
            second_max = max(second_max, arr[i])
    # return second_max


print(secondLargestElement([12, 35, 1, 10, 34]))  # 34
