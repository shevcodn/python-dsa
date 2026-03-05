def combination_sum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]

    return dp[target]

print(combination_sum4([1,2,3], 4))
print(combination_sum4([9], 3))
print(combination_sum4([1,2,3], 0))
