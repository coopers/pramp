def deletion_distance(str1, str2):
    lil, big = (str1, str2) if len(str1) < len(str2) else (str2, str1)
    L, B = len(lil), len(big)
    prev = None
    for b in reversed(range(B + 1)):
        cur = [0] * (L + 1)
        for l in reversed(range(L + 1)):
            if b == B:
                cur[l] = L - l
            elif l == L:
                cur[l] = B - b
            elif lil[l] == big[b]:
                cur[l] = prev[l + 1]
            else:
                cur[l] = 1 + min(cur[l + 1], prev[l])

        prev = cur
        
    return prev[0]