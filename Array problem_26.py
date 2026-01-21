'''
Problem Statement:
Given an array and a target sum K, count the number of pairs whose sum equals K.

Example

Input: arr = [1, 5, 7, -1, 5], K = 6
Output: 3
'''
def count_pairs(arr, K):
    freq = {}
    count = 0

    for num in arr:
        if K - num in freq:
            count += freq[K - num]
        freq[num] = freq.get(num, 0) + 1

    return count

print(count_pairs([1, 5, 7, -1, 5], 6))

