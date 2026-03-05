def remove_duplicates(nums):
    if not nums:
        return 0
    
    write = 0

    for i in range(write, len(nums)):
        if nums[i] != nums[write]:
            write += 1
            nums[write] = nums[i]

    return write + 1

print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates([1, 2, 3]))