def can_jump(nums):
    max_reach = 0

    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)

    return True

print(can_jump([2,3,1,1,4]))
print(can_jump([3,2,1,0,4]))
print(can_jump([1]))
print(can_jump([0]))