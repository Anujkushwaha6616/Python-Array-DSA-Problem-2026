'''
Problem Statement:

You are given an array and an integer k.
Find the maximum possible sum of any contiguous subarray of size k.

This is a classic sliding-window problem.

Example

Input:
arr = [2, 1, 5, 1, 3, 2]
k = 3

Output:
9
'''
def max_sum_subarray_k(arr, k):
    if k > len(arr):
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray_k(arr, k))

