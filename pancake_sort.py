def pancake_sort(arr):
    n = len(arr)
    while n > 1:
        m = max_index(arr, n)
        if m != n - 1:
            if m != 0:
                flip(arr, m)
            flip(arr, n - 1)
        n -= 1
    return arr
        
def flip(arr, k):
    j = 0
    while j < k:
        arr[j], arr[k] = arr[k], arr[j]
        j += 1
        k -= 1

def max_index(arr, k):
    res = 0
    for i in range(k):
        if arr[i] > arr[res]:
            res = i
    return res

arr = [1, 5, 4, 3, 2]
res = [1, 2, 3, 4, 5]
assert pancake_sort(arr) == res