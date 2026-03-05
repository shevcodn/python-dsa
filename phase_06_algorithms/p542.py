def stoneGame(piles):
    n = len(piles)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
    return dp[0][n - 1] > 0

print(stoneGame([5, 3, 4, 5]))
print(stoneGame([3, 7, 2, 3]))
print(stoneGame([1, 2]))
print(stoneGame([2, 1, 6, 3]))

