def max_product(nums):
    result = max(nums)
    cur_min = 1
    cur_max = 1

    for num in nums:
        if num == 0:
            cur_min, cur_max = 1, 1
            continue

        temp = cur_max
        cur_max = max(num, temp * num, cur_min * num)
        cur_min = min(num, temp * num, cur_min * num)
        result = max(result, cur_max)

    return result

print(max_product([2, 3, -2, 4]))
print(max_product([-2, 0, -1]))
print(max_product([-2, 3, -4]))
print(max_product([-2, -3, -4, -5]))