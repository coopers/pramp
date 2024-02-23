import heapq

def sort_k_messed_array(arr, k):
    n = len(arr)
    res = []
    h = arr[:k + 1]
    heapq.heapify(h)
    for i in range(k + 1, n):
        res.append(heapq.heapreplace(h, arr[i]))

    while h:
        res.append(heapq.heappop(h))

    return res

# test
arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert sort_k_messed_array(arr, k) == output