def selection_sort(arr):
    n = len(arr)
    for i in range(n):

        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [29, 10, 14, 37, 13, 19]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
