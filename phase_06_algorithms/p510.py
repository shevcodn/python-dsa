def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]

print(can_partition([1,5,11,5]))
print(can_partition([1,2,3,5]))
print(can_partition([1,1]))
print(can_partition([1,2,5]))

