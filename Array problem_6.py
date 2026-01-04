def two_sum(arr,target):
    seen = set()

    for num in arr:
        needed = target - num
        if needed in seen:
            return num,needed
        seen.add(num)
    return None
#Example use
arr=[2, 7, 11, 15]
target = 9
print(two_sum(arr,target))
