def bracket_match(text):
  opening = closing = 0
  for b in text:
    if b == '(':
      opening += 1
    else:
      if opening > 0:
        opening -= 1
      else:
        closing += 1
        
  return opening + closing

assert bracket_match('(()') == 1
assert bracket_match('(())') == 0
assert bracket_match('())(') == 2