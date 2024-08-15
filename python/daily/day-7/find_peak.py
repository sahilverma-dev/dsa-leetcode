# TODO revisit

# Question 1: Find Peak Element
# Problem Statement:
# A peak element in an array is an element that is greater than its neighbors. Given an input array nums where nums[i] ≠ nums[i+1], find a peak element and return its index. The array may contain multiple peaks; return the index of any peak.

from typing import List


def find_peak(nums: List):
    peak = float("-inf")
    for i in nums:
        peak = max(peak, i)
    return nums.index(peak)


print(find_peak([1, 2, 3, 1]))  # Output: 2 (index of peak element 3)
print(find_peak([1, 2, 1, 3, 5, 6, 4]))  # Output: 5 (index of peak element 6)


"""
find the maximum element and return its index
"""
