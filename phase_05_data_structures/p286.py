def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
print(nums)

nums = [1, 2, 3]
rotate(nums, 1)
print(nums)
