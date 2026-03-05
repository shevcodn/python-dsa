def max_subarray(nums):
    curr = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        curr = max(nums[i], curr + nums[i])
        best = max(best, curr)

    return best

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray([1]))
print(max_subarray([-1,-2,-3]))
print(max_subarray([5,4,-1,7,8]))