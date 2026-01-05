'''
Problem:
Given an array of integers, rotate the array to the right by k steps.

Example:
Input: arr = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
'''
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # handle k > n
    return arr[-k:] + arr[:-k]


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Rotated Array:", rotate_array(arr, k))

