# https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16

# 624. Maximum Distance in Arrays

# You are given m arrays, where each array is sorted in ascending order.

# You can pick up two integers from two different arrays (each array picks one) and calculate the distance.
# We define the distance between two integers a and b to be their absolute difference |a - b|.

# Return the maximum distance.

from typing import List


def maxDistance(arrays: List[List[int]]) -> int:
    # brute force
    # ans = float("-inf")
    # max_array = []
    # min_array = []

    # for arr in arrays:
    #     max_num = float("-inf")
    #     min_num = float("inf")
    #     for i in arr:
    #         max_num = max(i, max_num)
    #         min_num = min(i, min_num)
    #     max_array.append(max_num)
    #     min_array.append(min_num)
    #     # print(min_num, min_num)

    # diff_array = []

    # for i in range(len(min_array)):
    #     for j in range(len(min_array)):
    #         if i != j:
    #             diff_array.append(abs(max_array[i] - min_array[j]))

    # for i in diff_array:
    #     ans = max(ans, i)

    # return ans

    # arrays are already sorted
    # ans = float("-inf")

    # max_array = []
    # min_array = []

    # for arr in arrays:
    #     min_array.append(arr[0])
    #     max_array.append(arr[-1])
    #     # print(arr[0], arr[-1])

    # diff_array = []

    # for i in range(len(min_array)):
    #     for j in range(len(min_array)):
    #         if i != j:
    #             diff_array.append(abs(max_array[i] - min_array[j]))

    # for i in diff_array:
    #     ans = max(ans, i)

    # return ans

    # from neetcode
    ans = 0
    cur_max, cur_min = arrays[0][-1], arrays[0][0]

    for i in range(1, len(arrays)):
        arr = arrays[i]
        ans = max(ans, max(arr[-1] - cur_min, cur_max - arr[0]))
        cur_max = max(cur_max, arr[-1])
        cur_min = min(cur_min, arr[0])

    return ans


# Example 1:
# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
print("Example 1:", maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))  # 4

# Example 2:
# Input: arrays = [[1],[1]]
# Output: 0
print("Example 2:", maxDistance([[1], [1]]))  # 0
print("Example 3:", maxDistance([[1, 4], [0, 5]]))  # 4
print("Example 4:", maxDistance([[1, 5], [3, 4]]))  # 3


# Constraints:

# m == arrays.length
# 2 <= m <= 105
# 1 <= arrays[i].length <= 500
# -104 <= arrays[i][j] <= 104
# arrays[i] is sorted in ascending order.
# There will be at most 105 integers in all the arrays.
