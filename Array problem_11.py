'''
Problem

You are given an array of size n containing numbers from 1 to n+1.
One number is missing. Find the missing number.

Example:
Input: [1, 2, 4, 5]
Output: 3
'''
def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum


# Example usage
arr = [1, 2, 4, 5]
print("Missing Number =", find_missing_number(arr))

