# Question 2: Intersection of Two Arrays
# Problem Statement: Given two arrays, nums1 and nums2, return an array containing unique elements that are present in both arrays.

from typing import List


def intersection(nums1: List, nums2: List):
    result = set()
    unique = set()

    for i in nums1:
        unique.add(i)

    for i in nums2:
        if i in unique:
            result.add(i)

    return list(result)


# Example:
print(intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [9, 4]
