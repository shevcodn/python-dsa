def move_zeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
    while left < len(nums):
            nums[left] = 0
            left += 1
    return nums
    
print(move_zeroes([0,1,0,3,12]))
print(move_zeroes([0,0,1]))