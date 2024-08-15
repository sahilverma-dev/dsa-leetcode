# TODO: revisit

# Question 2: Product of Array Except Self
# Problem Statement:
# Given an array nums of n integers, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

from typing import List


def product_except_self(nums: List):
    # n = len(nums)
    # result = []

    # brute force
    # for i in range(n):
    #     product = 1
    #     for j in range(n):
    #         if i != j:
    #             product *= nums[j]
    #     result.append(product)

    n = len(nums)
    result = []
    product = 1

    for i in range(n):
        product *= nums[i]
        # result.append(i)
    print(product)

    for i in range(n):
        print(product, nums[i])
        if product == 0 and nums[i] == 0:
            result.append(0)
        elif nums[i] == 0:
            result.append(product)
        else:
            result.append(product // nums[i])

    return result


# print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]

# make a new array
# calculate product of the given array
# loop on the given array and append the division of the current element to the product value to the new array
# now return the array
# note: this problem will not work if given array have any zero value ara ele/0 will give error
# improvement: if there are 2 zeros the the whole answer will be array of zeros
