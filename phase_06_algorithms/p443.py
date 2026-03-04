def min_subarray_len(target, arr):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left = left + 1

    return min_len if min_len != float('inf') else 0

print(min_subarray_len(6, [2,3,1,2,4,3]))
print(min_subarray_len(4, [1,4,4]))
print(min_subarray_len(11, [1,1,1,1,1]))