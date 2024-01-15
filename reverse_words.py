def reverse_words(arr):
  def reverse_chars(l, r):
    while l < r:
      arr[l], arr[r] = arr[r], arr[l]
      l += 1
      r -= 1
      
  reverse_chars(0, len(arr) - 1)
  l = 0
  for r in range(len(arr)):
    if arr[r][0] == ' ':
      reverse_chars(l, r - 1)
      l = r + 1
      
  reverse_chars(l, len(arr) - 1)
  return arr

arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
output = [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
           'm', 'a', 'k', 'e', 's', '  ',
           'p', 'e', 'r', 'f', 'e', 'c', 't' ]
assert reverse_words(arr) == output