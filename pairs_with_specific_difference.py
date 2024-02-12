def find_pairs_with_given_difference(arr, k):
    # x = y + k
    s = set(arr)
    return [[y + k, y] for y in arr if y + k in s]

arr = [0, -1, -2, 2, 1]
k = 1
res = [[1, 0], [0, -1], [-1, -2], [2, 1]]
assert find_pairs_with_given_difference(arr, k) == res

arr = [1, 7, 5, 3, 32, 17, 12]
k = 17
res = []
assert find_pairs_with_given_difference(arr, k) == res