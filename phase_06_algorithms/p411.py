def max_subarray(nums):
    current = best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best

def max_subarray_with_indices(nums):
    current = best = nums[0]
    temp_start = best_start = best_end = 0
    for i in range(1, len(nums)):
        if nums[i] > current + nums[i]:
            current = nums[i]
            temp_start = i
        else:
            current += nums[i]
        if current > best:
            best = current
            best_start = temp_start
            best_end = i
    return best, best_start, best_end

def max_product_subarray(nums):
    max_prod = min_prod = result = nums[0]
    for num in nums[1:]:
        candidates = (num, max_prod * num, min_prod * num)
        max_prod = max(candidates)
        min_prod = min(candidates)
        result = max(result, max_prod)
    return result

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([1]))
print(max_subarray([-1, -2, -3]))
print(max_subarray([5, 4, -1, 7, 8]))

value, start, end = max_subarray_with_indices([100, -50, 200, -10, 300, -200, 50])
print(f"Max gain: ${value}, days {start} to {end}")

daily_returns = [2.1, -0.8, 3.4, -1.2, 4.5, -0.3, 1.8, -5.0, 2.2]
print(f"Best consecutive return period: {max_subarray(daily_returns):.1f}%")

print(max_product_subarray([2, 3, -2, 4]))
print(max_product_subarray([-2, 0, -1]))
