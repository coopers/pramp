import math

def drawLine(x0, x1, y0, y1):
  # draws line
  pass
  
def drawHTree(x, y, length, depth):
  if depth <= 0:
    return
  
  half = length // 2
  l = x - half
  r = x + half
  t = y - half
  b = y + half
  
  # draw an H
  drawLine(l, r, y, y)
  drawLine(l, l, t, b)
  drawLine(r, r, t, b)
  
  # draw next 4 HTrees
  length /= math.sqrt(2)
  depth -= 1
  drawHTree(l, t, length, depth)
  drawHTree(l, b, length, depth)
  drawHTree(r, t, length, depth)
  drawHTree(r, b, length, depth)
