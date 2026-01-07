'''
Problem

Given an array of integers, find the maximum product of a contiguous subarray.

Example:
Input: [2, 3, -2, 4]
Output: 6
(Subarray: [2, 3])
'''
def max_product_subarray(arr):
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        current = arr[i]

        temp_max = max(current, max_prod * current, min_prod * current)
        min_prod = min(current, max_prod * current, min_prod * current)
        max_prod = temp_max

        result = max(result, max_prod)

    return result


# Example usage
arr = [2, 3, -2, 4]
print("Maximum Product Subarray =", max_product_subarray(arr))
