def root(x, n):
    lo = float(0)
    hi = float(x)
    while True:
        mid = lo + (hi - lo) / float(2)
        val = mid ** n
        if abs(val - x) <= 0.001:
            return mid

        if val < x:
            lo = mid
        else:
            hi = mid