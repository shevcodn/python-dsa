def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def rob_linear(houses):
        if not houses:
            return 0
        prev2, prev1 = 0, 0
        for h in houses:
            prev2, prev1 = prev1, max(prev1, prev2 + h)
        return prev1
    
    return max(
        rob_linear(nums[:-1]),
        rob_linear(nums[1:])
    )

print(rob([2, 3, 2]))
print(rob([1, 2, 3, 1]))
print(rob([1, 2, 3]))
print(rob([1]))