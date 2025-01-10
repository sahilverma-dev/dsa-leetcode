def linear_search(nums, k):
    for i, num in enumerate(nums):
        if num == k:
            return i
    return -1


print(linear_search([1, 2, 3, 4, 5, 6], 4))
