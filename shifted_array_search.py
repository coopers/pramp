def shifted_arr_search(a, n):
    l, r = 0, len(a) - 1
    while True:
        if l > r:
            return -1
        
        m = l + (r - l) // 2
        if a[m] == n:
            return m
        if a[m] <= a[r]:
            if a[m] < n <= a[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            if a[l] <= n < a[m]:
                r = m - 1
            else:
                l = m + 1

assert shifted_arr_search([9, 12, 17, 2, 4, 5], 2) == 3