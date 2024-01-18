def get_different_number(arr):    
    n = len(arr)
    for i in range(n):
        while arr[i] < n:
            j = arr[i]
            if arr[j] == j:
                break
            arr[i], arr[j] = arr[j], arr[i]

    for i, num in enumerate(arr):
        if i != num:
            return i

    return n

assert get_different_number([0, 1, 2, 3]) == 4
assert get_different_number([0, 0, 2, 3]) == 1
