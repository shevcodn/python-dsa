def climb_stairs(n):
    if n <= 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
print(climb_stairs(5))