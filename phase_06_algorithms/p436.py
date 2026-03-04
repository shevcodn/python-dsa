def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left = left + 1
        else:
            right = right - 1

    return []

print(two_sum_sorted([1, 2, 3, 4, 6], 6))
print(two_sum_sorted([2, 7, 11, 15], 9))
print(two_sum_sorted([1, 2, 3], 10))


