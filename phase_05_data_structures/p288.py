def search(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]


print(search([3, 4, 5, 1, 2]))
print(search([4, 5, 6, 7, 0, 1, 2]))
print(search([1]))