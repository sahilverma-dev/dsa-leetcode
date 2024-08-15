# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

from typing import List


def removeDuplicates(nums: List[int]) -> int:

    # result = []

    # for num in nums:
    #     if result.count(num) < 2:
    #         result.append(num)

    # return result

    left = 0
    right = 0
    n = len(nums)

    while left < n:
        count = 1

        while left + 1 < n and nums[left] == nums[left + 1]:
            left += 1
            count += 1

        for i in range(min(count, 2)):
            nums[right] = nums[left]
            right += 1

        left += 1

    return right


print("Example 1:", removeDuplicates([1, 1, 1, 2, 2, 3]))  # 5, nums = [1,1,2,2,3,_]
print(
    "Example 2:", removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
)  # 7, nums = [0,0,1,1,2,3,3,_,_]
