def search_insert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
    
print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))
print(search_insert([1, 3, 5, 6], 7))
print(search_insert([1, 3, 5, 6], 0))

