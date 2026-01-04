def remove_duplicates(arr):
    if not arr:
        return []

    unique = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique.append(arr[i])

    return unique


# Example usage
arr = [1, 1, 2, 2, 3, 4, 4]
print(remove_duplicates(arr))
