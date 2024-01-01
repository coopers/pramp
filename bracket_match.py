def bracket_match(text):
  opening = closing = 0
  for b in text:
    if b == '(':
      closing += 1
    else:
      if closing > 0:
        closing -= 1
      else:
        opening += 1
        
  return opening + closing

assert bracket_match('(()') == 1
assert bracket_match('(())') == 0
assert bracket_match('())(') == 2