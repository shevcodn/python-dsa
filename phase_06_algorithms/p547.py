def eggDrop(k, n):
    dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        dp[i][0] = 0
        dp[i][1] = 1
    for j in range(1, n + 1):
        dp[1][j] = j
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            for x in range(1, j + 1):
                worst = 1 + max(dp[i-1][x-1], dp[i][j-x])
                dp[i][j] = min(dp[i][j], worst)
    return dp[k][n]

print(eggDrop(1, 10))
print(eggDrop(2, 10))
print(eggDrop(2, 100))
print(eggDrop(3, 14))