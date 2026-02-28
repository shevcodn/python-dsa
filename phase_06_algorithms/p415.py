def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit
    
def max_profit_two_transactions(prices):
    n = len(prices)
    left = [0] * n
    right = [0] * n
    min_p = prices[0]
    for i in range(1, n):
        min_p = min(min_p, prices[i])
        left[i] = max(left[i-1], prices[i] - min_p)
    max_p = prices[-1]
    for i in range(n-2, -1, -1):
        max_p = max(max_p, prices[i])
        right[i] = max(right[i+1], max_p - prices[i])
    return max(left[i] + right[i] for i in range(n))

print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([2, 4, 1]))

print(max_profit_two_transactions([3, 3, 5, 0, 0, 3, 1, 4]))
print(max_profit_two_transactions([1, 2, 3, 4, 5]))
