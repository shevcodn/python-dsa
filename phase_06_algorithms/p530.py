def rob_linear(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]

    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    return dp[-1]

def rob(houses):
    if len(houses) == 1:
        return houses[0]
    
    varA = rob_linear(houses[:-1])
    varB = rob_linear(houses[1:])

    return max(varA, varB)

print(rob([2, 3, 2]))
print(rob([1, 2, 3, 1]))
print(rob([1, 2, 3]))
print(rob([5]))
    