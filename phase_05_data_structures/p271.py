def max_subarray_sum(arr, k):
    max_sum = 0
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        if i >= k - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[i - (k - 1)]
    return max_sum


print(max_subarray_sum([1, 3, 2, 6, -1, 4, 1, 8, 2], 3))
print(max_subarray_sum([1, 2, 3, 4, 5], 2))
print(max_subarray_sum([2, 1, 5, 1, 3, 2], 3))
