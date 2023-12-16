def isToeplitz(arr):
    ROWS, COLS = len(arr), len(arr[0])
    return all(
        arr[r][c] == arr[r-1][c-1]
        for r in range(1, ROWS)
        for c in range(1, COLS)
    )