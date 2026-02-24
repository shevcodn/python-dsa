def min_subarray_len(nums, target):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

print(min_subarray_len([2,3,1,2,4,3], 7))
print(min_subarray_len([1,1,1,1,1], 11))
print(min_subarray_len([1,4,4], 4))