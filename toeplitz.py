def isToeplitz(arr):
    R, C = len(arr), len(arr[0])
    return all(arr[r][c] == arr[r-1][c-1] for r in range(1, R) for c in range(1, C))