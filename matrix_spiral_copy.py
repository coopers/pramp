def spiral_copy(m):
    res = []
    top = left = 0
    bottom = len(m) - 1
    right = len(m[0]) - 1
    while True:
        res.extend([m[top][i] for i in range(left, right + 1)])
        top += 1
        if top > bottom:
            break

        res.extend([m[i][right] for i in range(top, bottom + 1)])
        right -= 1
        if left > right:
            break

        res.extend([m[bottom][i] for i in reversed(range(left, right + 1))])
        bottom -= 1
        if top > bottom:
            break

        res.extend([m[i][left] for i in reversed(range(top, bottom + 1))])
        left += 1
        if left > right:
            break

    return res

matrix = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11,12, 13, 14, 15],
    [16,17, 18, 19, 20]
]

assert spiral_copy(matrix) == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]