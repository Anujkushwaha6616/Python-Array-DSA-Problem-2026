'''
Problem:
Given an array of integers, check whether the array is sorted in ascending order or not.

Example 1:
Input: [1, 2, 3, 4, 5]
Output: Sorted

Example 2:
Input: [3, 1, 4, 2]
Output: Not Sorted
'''
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return "Not Sorted"
    return "Sorted"


# Example usage
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))

