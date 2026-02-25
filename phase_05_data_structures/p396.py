def can_jump(nums):
    if not nums:
        return False
    
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:
            return True
        
print(can_jump([2,3,1,1,4]))
print(can_jump([3,2,1,0,4]))
print(can_jump([1,0]))