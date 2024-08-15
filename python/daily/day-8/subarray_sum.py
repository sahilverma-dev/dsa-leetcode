# Question 3: Sub-array Sum Equals K
# Problem Statement: Given an array of integers nums and an integer k, return the total number of continuous sub-arrays whose sum equals k.


def sub_array_sum(nums, k):
    count = 0
    sum = 0
    n = len(nums)

    left, right = 0, n
    while left < right:

        # print(left)
        sum += nums[left]

        if sum == k:
            return count
        elif sum > k:
            count += 1
            left += 1
        elif sum < k:
            left += 1

    return count

    # count = 0
    # sum = 0
    # sum_count = {}

    # for i, num in enumerate(nums):
    #     sum += num
    #     sum_count[i] = sum

    #     print(sum_count)
    #     # if sum_count

    # return count


# Example:
# print(sub_array_sum([1, 1, 1], 2))  # Output: 2 ([1, 1] and [1, 1])
print(sub_array_sum([1, 2, 3], 3))  # Output: 2 ([1, 2] and [3])
