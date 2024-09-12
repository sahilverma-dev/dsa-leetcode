from typing import List


def runningSum(nums: List[int]) -> List[int]:
    # brute force
    ans = []
    curr = 0
    for i in nums:
        curr += i
        ans.append(curr)

    return ans


print("Example 1:", runningSum([1, 2, 3, 4]))  # [1,3,6,10]
print("Example 2:", runningSum([1, 1, 1, 1, 1]))  # [1,2,3,4,5]
print("Example 3:", runningSum([3, 1, 2, 10, 1]))  # [3,4,6,16,17]
