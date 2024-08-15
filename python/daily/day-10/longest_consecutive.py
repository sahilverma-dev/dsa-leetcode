# Question 1: Longest Consecutive Sequence
# Problem Statement:
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence. The algorithm should run in O(n) complexity.


from typing import List


def longest_consecutive(nums: List):
    # brute force
    if not nums:
        return 0

    nums.sort()
    count = 1
    max_count = 1

    n = len(nums)
    for i in range(1, n):

        diff = nums[i] - nums[i - 1]
        if diff == 1:
            count += 1
        elif diff > 1:
            count = 1
        if count > max_count:
            max_count = count
    return max_count


print(
    "Example 1:", longest_consecutive([100, 4, 200, 1, 3, 2])
)  # Output: 4 (The longest sequence is [1, 2, 3, 4])


print(
    "Example 2:", longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
)  # Output: 9 (The longest sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8])
print("Example 3:", longest_consecutive([1, 2, 3, 10, 11, 20, 21, 22, 23, 24, 25]))
# Output: 6 (The longest sequence is [20, 21, 22, 23, 24, 25])
