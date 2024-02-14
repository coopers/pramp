def diffBetweenTwoStrings(source, target):
    S, T = len(source), len(target)
    dp = [[0 for _ in range(T+1)] for _ in range(S+1)]
    for s in range(S):
        dp[s][T] = S - s

    for t in range(T):
        dp[S][t] = T - t
    
    for s in reversed(range(S)):
        for t in reversed(range(T)):
            if source[s] == target[t]:
                dp[s][t] = dp[s+1][t+1]
            else:
                dp[s][t] = 1 + min(dp[s+1][t], dp[s][t+1])
    
    res = []
    s = t = 0
    while s < S and t < T:
        if source[s] == target[t]:
            res.append(source[s])
            s += 1
            t += 1
        else:
            if dp[s+1][t] <= dp[s][t+1]:
                res.append('-' + source[s])
                s += 1
            else:
                res.append('+' + target[t])
                t += 1
    
    while s < S:
        res.append('-' + source[s])
        s += 1
    
    while t < T:
        res.append('+' + target[t])
        t += 1
    
    return res
