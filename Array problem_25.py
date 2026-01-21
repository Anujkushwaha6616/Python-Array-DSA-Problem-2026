'''
'''
def move_zeroes(arr):
    result = [x for x in arr if x != 0]
    zero_count = arr.count(0)
    return result + [0] * zero_count

print(move_zeroes([0, 3, 0, 5, 1]))
