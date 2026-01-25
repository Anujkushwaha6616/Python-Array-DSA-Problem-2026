'''
Problem: 

Given an array of integers, find the length of the longest continuous subarray where each element is strictly greater than the previous one.

Example
Input:  [1, 2, 2, 3, 4, 5]
Output: 4

'''
def longest_increasing_subarray(arr):
    max_len = 1
    curr_len = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1

    return max_len


arr = [1, 2, 2, 3, 4, 5]
print(longest_increasing_subarray(arr))

