from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    n = len(nums)
    l, r = 0, n - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return l


print("Example 1: ", searchInsert([1, 3, 5, 6], 5))  # 2
print("Example 2: ", searchInsert([1, 3, 5, 6], 2))  # 1
print(
    "Example 3: ",
    searchInsert([1, 3, 5, 6], 7),
)  # 4
