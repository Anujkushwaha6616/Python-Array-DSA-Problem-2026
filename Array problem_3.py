'''
Problem:
Given an array of integers, count how many times a given number appears in the array.

Example:
Array: [1, 2, 3, 2, 4, 2, 5]
Number to count: 2
Output: 3
'''
def count_occurrences(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count


# Example usage
arr = [1, 2, 3, 2, 4, 2, 5]
target = 2
print("Count =", count_occurrences(arr, target))
