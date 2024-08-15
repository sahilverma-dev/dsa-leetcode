"""
Question 3: Find All Triplets with Zero Sum
Problem Statement:
Given an array nums of n integers, find all unique triplets (three numbers, a, b, c) in nums such that a + b + c = 0. The solution set must not contain duplicate triplets.
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []

    for i in range(len(nums)):
        j, k = i + 1, len(nums) - 1

        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif sum < 0:
                j += 1
            else:
                k -= 1

            # print(j, k)

    return ans


# Test cases
print(three_sum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 0, 0, 0]))  # Output: [[0, 0, 0]]
