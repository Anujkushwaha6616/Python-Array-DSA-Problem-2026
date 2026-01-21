'''
Problem:
Given an array, move all zeroes to the end without changing the order of non-zero elements.

Example

Input: [0, 3, 0, 5, 1]
Output: [3, 5, 1, 0, 0]
'''
def move_zeroes(arr):
    result = [x for x in arr if x != 0]
    zero_count = arr.count(0)
    return result + [0] * zero_count

print(move_zeroes([0, 3, 0, 5, 1]))


