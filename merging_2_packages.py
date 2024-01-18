def get_indices_of_item_wights(arr, limit):
    complementsOfLimit = {}
    for i, n in enumerate(arr):
        if n in complementsOfLimit:
            return [i, complementsOfLimit[n]]
        complementsOfLimit[limit - n] = i
    return []

arr = [4, 6, 10, 15, 16]
limit = 21
output = [3, 1]
assert get_indices_of_item_wights(arr, limit) == output