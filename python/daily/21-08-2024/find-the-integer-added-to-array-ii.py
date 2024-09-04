# https://leetcode.com/problems/find-the-integer-added-to-array-ii/description/
# 3132. Find the Integer Added to Array II
# Medium
# Topics
# Companies
# Hint
# You are given two integer arrays nums1 and nums2.

# From nums1 two elements have been removed, and all other elements have been increased (or decreased in the case of negative) by an integer, represented by the variable x.

# As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.

# Return the minimum possible integer x that achieves this equivalence.


# Example 1:

# Input: nums1 = [4,20,16,12,8], nums2 = [14,18,10]

# Output: -2

# Explanation:

# After removing elements at indices [0,4] and adding -2, nums1 becomes [18,14,10].

# Example 2:

# Input: nums1 = [3,5,5,3], nums2 = [7,7]

# Output: 2

# Explanation:

# After removing elements at indices [0,3] and adding 2, nums1 becomes [7,7].


# Constraints:

# 3 <= nums1.length <= 200
# nums2.length == nums1.length - 2
# 0 <= nums1[i], nums2[i] <= 1000
# The test cases are generated in a way that there is an integer x such that nums1 can become equal to nums2 by removing two elements and adding x to each element of nums1.

from typing import List
from collections import Counter


def minimumAddedInteger(nums1: List[int], nums2: List[int]) -> int:
    nums1.sort()
    nums2.sort()

    # Initialize the minimum difference as a large number
    min_diff = 0

    # Iterate over each element in nums1
    for i in range(len(nums1)):
        # Try to match each element in nums1 with each element in nums2
        for j in range(len(nums2)):
            diff = nums2[j] - nums1[i]
            if diff < 0:
                # Skip negative differences since we need positive x
                continue

            # Check if adding this diff to all elements in nums1 makes nums1 a subset of nums2
            transformed_nums1 = set(num + diff for num in nums1)
            if transformed_nums1.issubset(nums2):
                min_diff = min(min_diff, diff)

    return min_diff


# if min_diff != float("inf") else -1


print(
    "Example 1:", minimumAddedInteger(nums1=[4, 20, 16, 12, 8], nums2=[14, 18, 10])
)  # -2
# print("Example 2:", minimumAddedInteger(nums1=[3, 5, 5, 3], nums2=[7, 7]))  # 2

# print(
#     "Example 3:",
#     minimumAddedInteger(
#         nums1=[4, 6, 3, 1, 4, 2, 10, 9, 5], nums2=[5, 10, 3, 2, 6, 1, 9]
#     ),
# )  # 0
