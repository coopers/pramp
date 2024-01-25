def sudoku_solve(board):
  row = [set() for _ in range(9)]
  col = [set() for _ in range(9)]
  box = [set() for _ in range(9)]
  remaining = []
  for r in range(9):
    for c in range(9):
      if board[r][c] == '.':
        remaining.append((r, c))
      else:
        n = board[r][c]
        b = r // 3 * 3 + c // 3
        if (
          n in row[r] or
          n in col[c] or
          n in box[b]
        ):
          return False
        
        row[r].add(n)
        col[c].add(n)
        box[b].add(n)

  def helper():
    if not remaining:
      return True
    
    r, c = remaining.pop()
    b = r // 3 * 3 + c // 3
    s = {str(n) for n in range(1, 10)}
    s -= row[r]
    s -= col[c]
    s -= box[b]
    if not s:
      remaining.append((r, c))
      return False
    
    for guess in s:
      row[r].add(guess)
      col[c].add(guess)
      box[b].add(guess)
      if helper():
        return True

      row[r].remove(guess)
      col[c].remove(guess)
      box[b].remove(guess)
    return False
  
  return helper()