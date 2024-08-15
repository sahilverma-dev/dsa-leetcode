from typing import List


# Question 3: Move Zeroes
# Problem Statement:
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.


def move_zeroes(nums: List):
    n = len(nums)
    new_array = []
    count = 0
    for i in nums:
        if i != 0:
            count += 1
            new_array.append(i)

    for i in range(n - len(new_array)):
        new_array.append(0)

    return new_array


print(move_zeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(move_zeroes([0, 0, 1]))  # Output: [1, 0, 0]


# make a new array
# iterate through the array and append non zero values to the new array
# now subtract and length of new array to the given array's length to get the numbers of zeros
# now loop on the sub subtracted value to add remaining zeros
# now return the new array
