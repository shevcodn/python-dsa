def min_cost_climbing(cost):
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])

print(min_cost_climbing([10, 15, 20]))
print(min_cost_climbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(min_cost_climbing([0, 0]))