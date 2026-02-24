def max_ones(nums, k):
    left = 0
    max_ones = 0
    zeros_count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_count += 1
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1
        max_ones = max(max_ones, right - left + 1)
    return max_ones

print(max_ones([1,1,1,0,0,0,1,1,1,1,0], 2))
print(max_ones([0,0,1,1,1,0,0,1,1,0,0,0], 3))