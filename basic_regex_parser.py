def is_match(text, pattern):
    T, P = len(text), len(pattern)

    def helper(t, p):
        # end of pattern
        if p == P:
            return t == T

        # end of text
        if t == T:
            if p < P - 1 and pattern[p + 1] == '*':
                return helper(t, p + 2)
            return False

        # pattern with asterisk
        if p < P - 1 and pattern[p + 1] == '*':
            if pattern[p] in ('.', text[t]):
                return helper(t + 1, p) or helper(t, p + 2)
            return helper(t, p + 2)

        # pattern without asterisk
        if pattern[p] in ('.', text[t]):
            return helper(t + 1, p + 1)
        return False

    return helper(0, 0)

assert is_match("aa", "a") == False
assert is_match("aa", "aa") == True
assert is_match("abc", "a.c") == True
assert is_match("abbb", "ab*") == True
assert is_match("acd", "ab*c.") == True