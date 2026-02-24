def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

print(find_min([3,4,5,1,2]))
print(find_min([4,5,6,7,0,1,2]))
print(find_min([11,13,15,17]))