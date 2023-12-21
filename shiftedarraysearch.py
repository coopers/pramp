def shifted_arr_search(arr, num):
    l, r = 0, len(arr) - 1
    while True:
        if l > r:
            return -1
        
        m = l + (r - l) // 2
        if arr[m] == num:
            return m
        if arr[m] <= arr[r]:
            if arr[m] < num <= arr[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            if arr[l] <= num < arr[m]:
                r = m - 1
            else:
                l = m + 1