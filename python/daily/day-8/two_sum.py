# Question 1: Two Sum
# Problem Statement: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# Example:


from typing import List


def two_sum(nums: List, target):
    # temp = set()
    # for i, num in enumerate(nums):
    #     ele = target - num
    #     if ele in temp:
    #         return [nums.index(ele), i]
    #     temp.add(num)

    map = {}

    for i, num in enumerate(nums):

        diff = target - num
        if diff in map:
            return [map[diff], i]
        else:
            map[num] = i

    return []


print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1] (nums[0] + nums[1] = 2 + 7 = 9)
print(two_sum([3, 2, 4], 6))  # Output: [1, 2] (nums[1] + nums[2] = 2 + 4 = 6)
