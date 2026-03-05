def maxProfit(prices):
    if not prices:
        return 0
    hold = -prices[0]
    sold = 0
    rest = 0
    for i in range(1, len(prices)):
        prev_hold = hold
        prev_sold = sold
        prev_rest = rest
        hold = max(prev_hold, prev_rest - prices[i])
        sold = prev_hold + prices[i]
        rest = max(prev_rest, prev_sold)
    return max(sold, rest)

print(maxProfit([1, 2, 3, 0, 2]))
print(maxProfit([1]))
print(maxProfit([2, 1]))
print(maxProfit([6, 1, 3, 2, 4, 7]))