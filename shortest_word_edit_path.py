from collections import defaultdict

def get_transforms(word):
  return [word[:i] + '*' + word[i+1:] for i in range(len(word))]

def shortestWordEditPath(source, target, words):
  s = set(words)
  if target not in s:
    return -1
  
  d = defaultdict(set)
  for word in s:
    for transform in get_transforms(word):
      d[transform].add(word)

  words = set()
  words.add(source)
  count = 0
  while words:
    if target in words:
      return count
    
    count += 1
    transforms = {transform for word in words for transform in get_transforms(word) if transform in d}
    words = {word for transform in transforms for word in d[transform]}
    for transform in transforms:
      d.pop(transform)

  return -1

source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
output = 5
assert shortestWordEditPath(source, target, words) == output

source = "no"
target = "go"
words = ["to"]
output = -1
assert shortestWordEditPath(source, target, words) == output