def subarray(nums, k):
    counts = {0: 1}
    prefix = 0
    result = 0
    for num in nums:
        prefix += num
        result += counts.get(prefix - k, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return result

print(subarray([1,1,1], 2))
print(subarray([1,2,3], 3))
print(subarray([-1,-1,1], 0))
