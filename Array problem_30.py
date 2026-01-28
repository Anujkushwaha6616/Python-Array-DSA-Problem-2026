def count_subarrays_sum_k(arr, K):
    count = 0
    prefix = 0
    freq = {0: 1}

    for num in arr:
        prefix += num
        target = prefix - K

        if target in freq:
            count += freq[target]

        freq[prefix] = freq.get(prefix, 0) + 1

    return count


print(count_subarrays_sum_k([1, 1, 1], 2))
