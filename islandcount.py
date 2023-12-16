def get_number_of_islands(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
    count = 0
    def dfs(r, c):
        for dr, dc in DIRS:
            row, col = r + dr, c + dc
            if (
                0 <= row < ROWS and
                0 <= col < COLS and
                matrix[row][col]
            ):
                matrix[row][col] = 0
                dfs(row, col)

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c]:
                count += 1
                dfs(r, c)

    return count