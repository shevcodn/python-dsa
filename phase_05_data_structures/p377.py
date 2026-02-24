def find_range(nums, target):
    left = 0
    right = len(nums) - 1
    result = [-1, -1]

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            result[0] = mid
            result[1] = mid
            while result[0] > 0 and nums[result[0] -1] == target:
                result[0] -= 1
            while result[1] < len(nums) -1 and nums[result[1] + 1] == target:
                result[1] += 1
            break
    return result

print(find_range([5,7,7,8,8,10], 8))
print(find_range([5,7,7,8,8,10], 6))
print(find_range([1,1,1,1], 1))
