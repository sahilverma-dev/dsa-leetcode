# Question 3: Contains Duplicate II
# Problem Statement:
# Given an array of integers nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    # brute force solution
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] == nums[j] and abs(i - j) <= k:
    #             return True

    #  optimized solution
    map = {}
    for i, num in enumerate(nums):
        if num in map:
            if abs(i - map[num]) <= k:
                return True
        map[num] = i

    return False


print(
    contains_nearby_duplicate([1, 2, 3, 1], 3)
)  # Output: true (nums[0] = nums[3] and abs(0 - 3) = 3)
print(
    contains_nearby_duplicate([1, 0, 1, 1], 1)
)  # Output: true (nums[2] = nums[3] and abs(2 - 3) = 1)
print(
    contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2)
)  # Output: false (No such pair with abs(i - j) <= 2)
