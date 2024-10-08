# https://leetcode.com/problems/combination-sum/description/


# 39. Combination Sum
# Medium
# Topics
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

    def fun(count: int, candidates: List[int], target: int):
        n = len(candidates)

        ans = []
        # base case
        if count == n:
            return ans

        # check for combinations
        for i in range(count, n):
            print(i, candidates[i])

        # recursive case
        return fun(count + 1, candidates, target)

    ans = fun(0, candidates, target)
    return ans


print("Example 1:", combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
