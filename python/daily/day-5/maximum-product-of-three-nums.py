"""
Question 3: Maximum Product of Three Numbers
Problem Statement: Given an integer array, find three numbers whose product is maximum and return the maximum product.
"""

from typing import List


def maximum_product(nums: List):
    arr = []

    # for i in range(0, len(nums) - 2):
    #     arr.append(nums[i] * nums[i + 1] * nums[i + 2])

    # brute force

    # for i in nums:
    #     for j in nums:
    #         for k in nums:
    #             if i != j and j != k and k != i:
    #                 arr.append(i * j * k)

    # max_ele = float("-inf")
    # for i in arr:
    #     max_ele = max(max_ele, i)

    # return max_ele

    # classic python solution
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


print(maximum_product([1, 2, 3]))  # Output: 6
print(maximum_product([1, 2, 3, 4]))  # Output: 24
print(maximum_product([-1, -2, -3, -4]))  # Output: -6
print(maximum_product([-4, -3, -2, -1, 60]))  # Output: 720
print(maximum_product([-10, -20, -30, -20, -40, -60]))  # Output: -4000
