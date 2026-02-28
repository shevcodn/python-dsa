def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1, 5, 10, 25], 36))

print(coin_change_ways([1, 2, 5], 5))
print(coin_change_ways([2], 3))