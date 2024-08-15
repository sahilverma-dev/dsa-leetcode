from typing import List


def removeElement(nums: List[int], val: int) -> int:
    # ans = []
    # for i in nums:
    #     if i != val:
    #         ans.append(i)

    # return len(ans)
    # two pointers with while
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]
            nums[right] = nums[left]
            right -= 1
        else:
            left += 1
    return left


print("Example 1:", removeElement([3, 2, 2, 3], 3))  # Output: 2, nums = [2,2,_,_]
print(
    "Example 2:", removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
)  # Output: 5, nums = [0,1,4,0,3,_,_,_]

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
