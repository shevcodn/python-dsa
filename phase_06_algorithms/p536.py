def jump(nums):
    jumps = 0
    farthest = 0
    end = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == end:
            jumps += 1
            end = farthest
    
    return jumps

print(jump([2, 3, 1, 1, 4]))
print(jump([2, 3, 0, 1, 4]))
print(jump([1, 2, 3]))
print(jump([1, 1, 1, 1]))