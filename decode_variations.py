def decodeVariations(S):
    pre = None
    cur = one = two = 1
    for i in reversed(range(len(S))):
        ch = S[i]
        cur = 0 if ch == '0' else one
        if pre is not None and (ch == '1' or (ch == '2' and '0' <= pre <= '6')):
            cur += two

        one, two, pre = cur, one, ch

    return one