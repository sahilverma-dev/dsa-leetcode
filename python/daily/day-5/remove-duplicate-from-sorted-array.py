"""
Question 2: Remove Duplicates from Sorted Array 
Problem Statement: Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    # brute force
    # unique = set()
    # for i in nums:
    #     unique.add(i)

    # return len(list(unique))
    count = 0
    for i in range(1, len(nums)):
        # print(nums[i], nums[i - 1])
        if nums[i] == nums[i - 1]:
            count += 1

    return len(nums) - count


print(removeDuplicates([1, 1, 2, 3, 4, 5, 5]))  # 5
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # 5
print(removeDuplicates([1, 2, 3]))  # 5
