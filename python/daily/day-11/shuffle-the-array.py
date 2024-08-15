# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customers wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.


from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    # Brute force
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i + n])
    return ans


# Example 1:

# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
print(shuffle([2, 5, 1, 3, 4, 7], 3))  # Output: [2,3,5,4,1,7]

# Example 2:
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))  # Output: [1,4,2,3,3,2,4,1]

# Example 3:
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
print(shuffle([1, 1, 2, 2], 2))  # Output: [1,2,1,2]
