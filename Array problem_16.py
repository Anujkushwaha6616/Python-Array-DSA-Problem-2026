'''
Problem

Given an array and a value K, find the length of the longest subarray whose sum equals K.

Example

Input:
arr = [1, 2, 3, 1, 1, 1, 5], K = 5
Output:
3
'''
def longest_subarray_with_sum_k(arr, k):
    prefix_sum = 0
    seen = {}
    max_len = 0

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum == k:
            max_len = i + 1

        if prefix_sum - k in seen:
            max_len = max(max_len, i - seen[prefix_sum - k])

        if prefix_sum not in seen:
            seen[prefix_sum] = i

    return max_len

# Example
print(longest_subarray_with_sum_k([1, 2, 3, 1, 1, 1, 5], 5))

