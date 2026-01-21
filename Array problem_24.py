'''
Problem:
Given an integer array, find the second largest distinct element. If it doesn’t exist, return -1.

Example

Input: [4, 1, 9, 7, 9]
Output: 7
'''
def second_largest(arr):
    unique = list(set(arr))
    if len(unique) < 2:
        return -1
    unique.sort()
    return unique[-2]

print(second_largest([4, 1, 9, 7, 9]))


