def matrixChain(dims):
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]

print(matrixChain([10, 30, 5, 60]))
print(matrixChain([40, 20, 30, 10, 30]))
print(matrixChain([10, 20, 30]))
print(matrixChain([5, 10 ,3, 12, 5, 50]))