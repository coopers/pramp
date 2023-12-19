def num_of_paths_to_dest(n):
    cur = [1] * n
    nxt = [1] * n
    for i in range(1, n):
        for j in range(i+1, n):
            nxt[j] = nxt[j-1] + cur[j]

        cur = nxt

    return cur[-1]
