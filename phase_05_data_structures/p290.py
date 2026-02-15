def count_occurrences(nums, target):
    count = 0
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            count += 1

            i = mid - 1
            while i >= 0 and nums[i] == target:
                count += 1
                i -= 1
            j = mid + 1
            while j < len(nums) and nums[j] == target:
                count += 1
                j += 1
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return count

print(count_occurrences([1, 2, 2, 2, 3, 4], 2))
print(count_occurrences([1, 1, 1, 1, 1], 1))
print(count_occurrences([1, 2, 3], 4))