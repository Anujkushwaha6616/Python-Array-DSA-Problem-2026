'''
Problem:
Given an array of integers, find the sum of the contiguous subarray with the largest sum.

Example:
Input: [−2, 1, −3, 4, −1, 2, 1, −5, 4]
Output: 6 (subarray [4, −1, 2, 1])
'''
def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum =", max_subarray_sum(arr))

