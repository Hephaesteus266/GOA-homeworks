def manual_sum(arr):
    result = 0
    for i in arr:
        result += i
    return result

print(manual_sum([1,2,3,4,5,6]))

def manual_max(arr):
    max_val = arr[0]
    for i in arr:
        if i > max_val:
            max_val = i
    return max_val

print(manual_max([1,2,3,4,5,6]))

def manual_min(arr):
    min_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
    return min_val

print(manual_min([1,2,3,4,5,6]))

def manual_len(arr):
    result = 0
    for i in arr:
        result += 1
    return result

print(manual_len([1,2,3,4,5,6]))

def manual_reduce(arr):
    copied_arr = []
    for i in arr:
        copied_arr.append(i)
    return copied_arr

Origin_arr = [1,2,3,4,4,6,7]
print(Origin_arr)
print(manual_reduce(Origin_arr))