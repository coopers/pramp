# time: O(n log n)
# space: O(1)

#lambda function
def absSort(arr):
  arr.sort(key=lambda n: (abs(n), n))
  return arr

#compare function
def compare(a, b):
  if abs(a) < abs(b):
    return -1
  if abs(a) > abs(b):
    return 1
  if a < b:
    return -1
  if a > b:
    return 1
  return 0

def absSort(arr):
  arr.sort(cmp=compare)
  return arr

