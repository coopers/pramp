def decodeVariations(S):
    pre = None
    cur = one = two = 1
    for i in reversed(range(len(S))):
        ch = S[i]
        if ch == '0':
            cur = 0
        else:
            cur = one
            if pre is not None and (ch == '1' or (ch == '2' and '0' <= pre <= '6')):
                cur += two

        pre = ch
        one, two = cur, one

    return one