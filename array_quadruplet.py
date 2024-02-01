def find_array_quadruplet(arr, s):
    N = len(arr)
    arr.sort()
    for i, n in enumerate(arr[:-3]):
        triple_sum = s - n
        for j in range(i + 1, N - 2):
            double_sum = triple_sum - arr[j]
            l = j + 1
            r = N - 1
            while l < r:
                total = arr[l] + arr[r]
                if total == double_sum:
                    return [arr[i], arr[j], arr[l], arr[r]]
                elif total < double_sum:
                    l += 1
                else:
                    r -= 1
    return []

arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
output = [0, 4, 7, 9]
assert find_array_quadruplet(arr, s) == output