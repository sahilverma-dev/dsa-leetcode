def merge_sorted_arrays(arr1, arr2):
    # brute force
    # new_set = set()
    # for i in arr1:
    #     new_set.add(i)
    # for i in arr2:
    #     new_set.add(i)

    # print(new_set)
    # return list(new_set)

    # other solution
    new_array = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_array.append(arr1[i])
            i += 1
        else:
            new_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        new_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        new_array.append(arr2[j])
        j += 1

    return new_array


print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(merge_sorted_arrays([0, 0, 0], [0, 0]))  # Output: [0, 0, 0, 0, 0]
print(merge_sorted_arrays([1, 2, 3], []))  # Output: [1, 2, 3]
