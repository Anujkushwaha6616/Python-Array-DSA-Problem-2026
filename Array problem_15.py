def first_missing_positive(arr):
    arr_set = set(arr)
    smallest = 1

    while smallest in arr_set:
        smallest += 1

    return smallest

# Example
print(first_missing_positive([3, 4, -1, 1]))

