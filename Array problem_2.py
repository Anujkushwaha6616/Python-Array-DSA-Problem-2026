'''
Problem:
Given an array of integers, find the largest and smallest element in the array.

Example:
Input: [4, 2, 9, 1, 12]
Output:
Smallest = 1
Largest = 12
'''
def find_min_max(arr):
    if not arr:
        return None

    smallest = arr[0]
    largest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest


# Example usage
arr = [4, 2, 9, 1, 12]
min_val, max_val = find_min_max(arr)
print("Smallest =", min_val)
print("Largest =", max_val)
