def get_different_number(arr):    
  def swap(i, j):
    arr[i], arr[j] = arr[j], arr[i]
  
  n = len(arr)
  for i in range(n):
    while True:
      j = arr[i]
      if j >= n or arr[j] == j:
        break
      swap(i, j)
  
  for i, num in enumerate(arr):
    if i != num:
      return i
    
  return n

assert get_different_number([0, 1, 2, 3]) == 4
