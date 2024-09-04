# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

# 1351. Count Negative Numbers in a Sorted Matrix
# Easy
# Topics
# Companies
# Hint
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.


# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100


# Follow up: Could you find an O(n + m) solution?

from typing import List


def countNegatives(grid: List[List[int]]) -> int:
    # brute force
    # count = 0
    # for row in grid:
    #     for cell in row:
    #         if cell < 0:
    #             count += 1
    # return count

    # with binary search
    count = 0

    for row in grid:
        n = len(row)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] < 0:
                right = mid - 1
            else:
                left = mid + 1
        # print(left, right)
        count += n - left

    return count


print(
    "Example 1: ",
    countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]),
)  # 8
# print("Example 1: ", countNegatives([[3, 2], [1, 0]]))  # 0
