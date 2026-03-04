def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(window_sum, max_sum)

    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
print(max_sum_subarray([1, 4, 2, 10, 2, 3], 4))
print(max_sum_subarray([1, 2, 3], 2))