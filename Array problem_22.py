'''
Problem

Given an unsorted array of distinct integers, find the minimum number of swaps required to sort the array in ascending order.

Input:
arr = [10, 19, 6, 3, 5]

Output:
2
'''
def min_swaps_to_sort(arr):
    n = len(arr)
    arr_with_index = [(arr[i], i) for i in range(n)]
    arr_with_index.sort()
    
    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or arr_with_index[i][1] == i:
            continue

        cycle_size = 0
        j = i
        
        # Count cycle length
        while not visited[j]:
            visited[j] = True
            j = arr_with_index[j][1]
            cycle_size += 1

        if cycle_size > 1:
            swaps += cycle_size - 1

    return swaps

# Example
arr = [10, 19, 6, 3, 5]
print(min_swaps_to_sort(arr))
