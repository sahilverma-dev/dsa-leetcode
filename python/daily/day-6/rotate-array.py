# Question 1: Rotate Array
# Problem Statement:
# Given an array, rotate the array to the right by k steps, where k is non-negative.
from typing import List


def rotate_array(nums: List, target) -> List:
    new_array = []
    n = len(nums)
    for i in range(n):
        # new_array.append(i)
        # print(i, target - i)
        # x = target - i
        x = (n - (target - i - 1) % n) - 1
        new_array.append(nums[x])
    return new_array


# Example:
print(rotate_array([1, 2, 3, 4, 5], 3))  # Output: [3, 4, 5, 1, 2]
print(rotate_array([-1, -100, 3, 99], 2))  # Output: [3, 99, -1, -100]
