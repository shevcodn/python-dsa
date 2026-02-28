def can_jump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True

def min_jumps(nums):
    jumps = curr_end = curr_farthest = 0
    for i in range(len(nums) - 1):
        curr_farthest = max(curr_farthest, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = curr_farthest
    return jumps
    
print(can_jump([2, 3, 1, 1, 4]))
print(can_jump([3, 2, 1, 0, 4]))
print(can_jump([0]))