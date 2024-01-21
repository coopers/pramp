def get_shortest_unique_substring(arr, s):
  counts = {n: 0 for n in arr}
  need = len(arr)
  l = 0
  res = ''
  for r in range(len(s)):
    if s[r] in counts:
      if counts[s[r]] == 0:
        need -= 1
      counts[s[r]] += 1
      while not need:
        if not res or r - l < len(res):
          res = s[l:r+1]
        if s[l] in counts:
          counts[s[l]] -= 1
          if counts[s[l]] == 0:
            need += 1
        l += 1
        
  return res

assert get_shortest_unique_substring(['x','y','z'], 'xyyzyzyx') == 'zyx'