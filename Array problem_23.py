'''
Given an array, find the length of the longest subarray where the difference between the maximum and minimum element is at most 1.

Example

Input:
arr = [1, 2, 2, 1, 3]

Explanation:

Subarray [1,2,2,1] → max = 2, min = 1 → diff = 1 → valid

Length = 4

Output:
4
'''
def longest_subarray(arr):
    left = 0
    max_len = 0

    for right in range(len(arr)):
        # Current window ke values
        window = arr[left:right+1]
        mn = min(window)
        mx = max(window)

        # Agar condition break ho jaaye, left ko aage badhao
        while mx - mn > 1:
            left += 1
            window = arr[left:right+1]
            mn = min(window)
            mx = max(window)

        # Max length update karo
        max_len = max(max_len, right - left + 1)

    return max_len


# Example
arr = [1, 2, 2, 1, 3]
print(longest_subarray(arr))  # Output: 4
