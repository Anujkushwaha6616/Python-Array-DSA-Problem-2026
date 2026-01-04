'''
Problem

Given an array of integers and a target value, find two numbers in the array whose sum is equal to the target.

Example:
Input: arr = [2, 7, 11, 15], target = 9
Output: (2, 7)
'''
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

