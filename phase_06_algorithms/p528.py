def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1, 5, 6], 11))
print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1], 0))