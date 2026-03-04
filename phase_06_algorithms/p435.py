def find_first(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def find_last(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def count_occurrences(arr, target):
    first = find_first(arr, target)
    if first == -1:
        return 0
    last = find_last(arr, target)
    return last - first + 1


print(count_occurrences([1, 3, 3, 3, 7], 3))
print(count_occurrences([1, 2, 4, 4, 4], 4))
print(count_occurrences([1, 2, 3], 9))