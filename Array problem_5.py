def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return "Not Sorted"
    return "Sorted"


# Example usage
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))
