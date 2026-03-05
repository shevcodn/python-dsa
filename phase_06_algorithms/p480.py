def subarray_sum(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}

    for num in nums:
        prefix += num
    
        if prefix - k in seen:
            count += seen[prefix - k]

        seen[prefix] = seen.get(prefix, 0) + 1

    return count

print(subarray_sum([1, 2, 3], 3))
print(subarray_sum([1, 1, 1], 2))
print(subarray_sum([1, -1, 1], 1))
print(subarray_sum([3], 3))