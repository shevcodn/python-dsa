def lis(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[1] = max(dp[i], dp[j] + 1)

    return max(dp)

print(lis([10, 9, 2, 5, 3, 7, 101, 18]))
print(lis([0, 1, 0, 3, 2, 3]))
print(lis([7, 7, 7, 7]))
print(lis([1]))