def move_zeroes(nums):
    write = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write] = nums[i]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1

    return nums

print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([0, 0, 1]))
print(move_zeroes([1, 2, 3]))