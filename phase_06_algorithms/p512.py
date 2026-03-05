def max_product(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        candidates = (nums[i], max_prod * nums[i], min_prod * nums[i])
        max_prod = max(candidates)
        min_prod = min(candidates)
        result = max(result, max_prod)

    return result


print(max_product([2, 3, -2, 4]))
print(max_product([-2, 0, -1]))
print(max_product([-2, 3, -4]))
print(max_product([-2]))
