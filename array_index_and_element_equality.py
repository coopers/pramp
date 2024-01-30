def index_equals_value_search(a):
    l, r = 0, len(a) - 1
    while l < r:
        m = l + (r - l) // 2
        if a[m] < m:
            l = m + 1
        elif a[m] == m:
            r = m
        else:
            r = m - 1

    return l if a[l] == l else -1