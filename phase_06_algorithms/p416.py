def rob(nums):
    prev_prev = 0
    prev = 0
    for num in nums:
        curr = max(num  + prev_prev, prev)
        prev_prev = prev
        prev = curr
    return prev

def rob_circular(nums):
    if len(nums) == 1:
        return nums[0]
    def rob_linear(arr):
        prev_prev = prev = 0
        for num in arr:
            prev_prev, prev = prev, max(num + prev_prev, prev)
        return prev
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))
print(rob([2, 1, 1, 2]))

print(rob_circular([2, 3, 2]))
print(rob_circular([1, 2, 3, 1]))