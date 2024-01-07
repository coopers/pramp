def moveZerosToEnd(arr):
  i = 0
  for j, n in enumerate(arr):
    if n != 0:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
  
  return arr
      
assert moveZerosToEnd([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]) == [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]