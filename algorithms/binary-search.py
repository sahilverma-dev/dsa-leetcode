def binary_search(nums, k):
    l, r = 0, len(nums)

    while l <= r:
        m = (l + r) // 2

        if k == nums[m]:
            return m
        elif k < m:
            r = m - 1
        else:
            l = m + 1

    return -1


print(binary_search([1, 2, 3, 4, 5, 6], 4))  # 3
