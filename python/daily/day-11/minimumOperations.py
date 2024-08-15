# 3190. Find Minimum Operations to Make All Elements Divisible by Three...
# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

# Return the minimum number of operations to make all elements of nums divisible by 3.
from typing import List


def minimumOperations(nums: List):
    count = 0
    for i in nums:
        rem = i % 3
        if rem == 1:
            count += 1
        elif rem == 2:
            count += 1
    return count


print(minimumOperations([1, 2, 3, 4]))  # 3
print(minimumOperations([3, 6, 9]))  # 0

# Example 1:

# Input: nums = [1,2,3,4]

# Output: 3

# Explanation:

# All array elements can be made divisible by 3 using 3 operations:

# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.
# Example 2:

# Input: nums = [3,6,9]

# Output: 0
