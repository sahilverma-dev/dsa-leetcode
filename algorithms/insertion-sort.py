from re import A


def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i - 1
        x = arr[i]

        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= i

        arr[j + 1] = x

    return arr


arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
