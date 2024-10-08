from typing import List


def minStartValue(nums: List[int]) -> int:
    # brute force
    # startValue = 1

    # while True:
    #     curr_sum = startValue
    #     valid = True

    #     for num in nums:
    #         curr_sum += num
    #         if curr_sum <= 0:
    #             valid = False
    #             break

    #     if valid:
    #         return startValue

    #     startValue += 1

    # prefix sum
    min_prefix_sum = float("inf")
    curr_prefix_sum = 0

    for num in nums:
        curr_prefix_sum += num

        if curr_prefix_sum < min_prefix_sum:
            min_prefix_sum = curr_prefix_sum

    return max(1, -min_prefix_sum + 1)


print("Example 1:", minStartValue([-3, 2, -3, 4, 2]))  # 5
print("Example 2:", minStartValue([1, 2]))  # 1
print("Example 3:", minStartValue([1, -2, -3]))  # 5
