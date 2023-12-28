import bisect
import math

def find_duplicates(lil, big):
    res = []
    if len(lil) > len(big):
        lil, big = big, lil

    L, B = len(lil), len(big)
    if L * math.log(B) / math.log(2) < L + B:
        for num in lil:
            i = bisect.bisect_left(big, num)
            if i == B:
                break
            if big[i] == num:
                res.append(num)
    else:
        l = b = 0
        while l < L and b < B:
            if lil[l] == big[b]:
                res.append(lil[l])
                l += 1
                b += 1
            elif lil[l] < big[b]:
                l += 1
            else:
                b += 1

    return res