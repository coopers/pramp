from collections import deque

def shortestCellPath(grid, sr, sc, tr, tc):   
    DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
    ROWS, COLS = len(grid), len(grid[0])
    visit = {(sr, sc)}
    q = deque([(sr, sc)])
    count = 0
    while q:
        for _ in range(len(q)):
            row, col = q.popleft()
            if row == tr and col == tc:
                return count
            for dr, dc in DIRECTIONS:
                r, c = row + dr, col + dc
                if (
                    0 <= r < ROWS and
                    0 <= c < COLS and
                    grid[r][c] and
                    (r, c) not in visit
                ):
                    visit.add((r, c))
                    q.append((r, c))
        count += 1

    return -1
        
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr, sc, tr, tc = 0, 0, 2, 0
assert shortestCellPath(grid, sr, sc, tr, tc) == 8