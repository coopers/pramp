def num_of_paths_to_dest(n):
    dp = [1] * n
    for i in range(1, n-1):
        for j in range(i+1, n):
            dp[j] += dp[j-1]

    return dp[-1]

assert num_of_paths_to_dest(4) == 5