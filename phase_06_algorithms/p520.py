def unique_paths_with_obstacles(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        if grid[i][0] == 1:
            break
        dp[i][0] = 1

    for j in range(n):
        if grid[0][j] == 1:
            break
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m-1][n-1]

print(unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(unique_paths_with_obstacles([[0,1],[0,0]]))
print(unique_paths_with_obstacles([[1]]))