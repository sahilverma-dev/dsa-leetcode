# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

from typing import List


def numIdenticalPairs(nums: List):
    # brute force
    # n = len(nums)
    # count = 0
    # for i in range(n):
    #     for j in range(n):
    #         if i != j and nums[i] == nums[j] and i < j:
    #             count += 1
    # return count

    # with map
    map = {}
    count = 0

    for num in nums:
        if num in map:  # have possibility to make a pair
            count += map[num]  # increase the count with current element in map
            map[num] += 1  # increase count in map for element's presence
        else:
            map[num] = 1  # initiate count

    # print(map)
    return count


# Example 1:

# Input: nums = [1,2,3,1,1,3]
print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # Output: 4
# Output: 4
# Explanation: There are 4 good pairs (0,3) [1,1] , (0,4) [1,1], (3,4) [1,2], (2,5) [3,3] 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
print(numIdenticalPairs([1, 1, 1, 1]))  # Output: 6
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
print(numIdenticalPairs([1, 2, 3]))  # Output: 0
