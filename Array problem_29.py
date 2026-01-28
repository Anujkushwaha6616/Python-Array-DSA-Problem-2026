def first_missing_positive(arr):
    arr_set = set(arr)
    num = 1

    while num in arr_set:
        num += 1

    return num


print(first_missing_positive([3, 4, -1, 1]))
