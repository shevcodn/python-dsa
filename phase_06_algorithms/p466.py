def remove_duplicates(nums):
    if not nums:
        return 0
    
    write = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[write - 1]:
            nums[write] = nums[i]
            write += 1

    return write

print(remove_duplicates([1, 1, 2, 3, 3]))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([1, 2, 3]))