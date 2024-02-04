def is_match(t, p):
    # reach end of pattern
    if len(p) == 0:
        return len(t) == 0

    # reach end of text
    if len(t) == 0:
        if len(p) > 1 and p[1] == '*':
            return is_match(t, p[2:])
        return False

    # pattern with asterisk
    if len(p) > 1 and p[1] == '*':
        if p[0] in ('.', t[0]):
            return is_match(t[1:], p) or is_match(t, p[2:])
        return is_match(t, p[2:])

    # pattern without asterisk
    if p[0] in ('.', t[0]):
        return is_match(t[1:], p[1:])
    return False

text = "aa"
pattern = "a"
assert is_match(text, pattern) == False

text = "aa"
pattern = "aa"
assert is_match(text, pattern) == True

text = "abc"
pattern = "a.c"
assert is_match(text, pattern) == True

text = "abbb"
pattern = "ab*"
assert is_match(text, pattern) == True

text = "acd"
pattern = "ab*c."
assert is_match(text, pattern) == True