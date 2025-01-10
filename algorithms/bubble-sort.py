def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums


print(bubble_sort([3, 5, 2, 7, 8, 78, 1]))
