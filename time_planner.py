def meeting_planner(A, B, dur):
    START, END = 0, 1
    a = b = 0
    while a < len(A) and b < len(B):
        start = max(A[a][START], B[b][START])
        end = min(A[a][END], B[b][END])
        if end - start >= dur:
            return [start, start + dur]

        if A[a][END] < B[b][END]:
            a += 1
        else:
            b += 1

    return []

A = [[10, 50], [60, 120], [140, 210]]
B = [[0, 15], [60, 70]]
dur = 8
output = [60, 68]
assert meeting_planner(A, B, dur) == output

A = [[10, 50], [60, 120], [140, 210]]
B = [[0, 15], [60, 70]]
dur = 12
output = []
assert meeting_planner(A, B, dur) == output