def array_of_array_products(arr):
    if len(arr) == 1:
        return []

    pre = 1
    res = []
    for n in arr:
        res.append(pre)
        pre *= n

    post = 1
    for i in range(len(arr) -1, -1, -1):
        res[i] *= post
        post *= arr[i]

    return res

assert array_of_array_products([8, 10, 2]) == [20, 16, 80]
assert array_of_array_products([2, 7, 3, 4]) == [84, 24, 56, 42]