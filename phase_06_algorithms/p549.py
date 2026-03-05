def mctFromLeafValues(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    max_val = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            max_val[i][j] = max(arr[i:j+1])
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + max_val[i][k] * max_val[k+1][j]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]

print(mctFromLeafValues([6, 2, 4]))
print(mctFromLeafValues([4, 11]))
print(mctFromLeafValues([1, 2, 3, 4]))
print(mctFromLeafValues([6, 2, 4, 3]))