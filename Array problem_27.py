
'''---

## ✅ Python Solution

```python'''
def more_than_n_by_k(arr, K):
    n = len(arr)
    freq = {}
    
    # Count frequency of each element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    result = []
    limit = n // K

    # Check which appear more than n/k times
    for num in freq:
        if freq[num] > limit:
            result.append(num)

    return result


# Example 1
arr1 = [1, 2, 6, 6, 6, 6, 6, 10]
K1 = 4
print(more_than_n_by_k(arr1, K1))  # Output: [6]

# Example 2
arr2 = [3, 4, 4, 5, 5, 5, 5]
K2 = 4
print(more_than_n_by_k(arr2, K2))  # Output: [4, 5]
