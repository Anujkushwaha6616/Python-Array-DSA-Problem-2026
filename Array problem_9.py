def move_zeroes(arr):
    index = 0

    for num in arr:
        if num != 0:
            arr[index] = num
            index += 1

    while index < len(arr):
        arr[index] = 0
        index += 1

    return arr

# Example usage
arr = [0, 1, 0, 3, 12]
print("After moving zeroes:", move_zeroes(arr))
