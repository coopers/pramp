def isToeplitz(arr):
    ROWS, COLS = len(arr), len(arr[0])
    return all(
        arr[r][c] == arr[r-1][c-1]
        for r in range(1, ROWS)
        for c in range(1, COLS)
    )

assert isToeplitz(
    [
        [1,2,3,4],
        [5,1,2,3],
        [6,5,1,2]
    ]
) == True

assert isToeplitz(
    [
        [1,2,3,4],
        [5,1,9,3],
        [6,5,1,2]
    ]
) == False