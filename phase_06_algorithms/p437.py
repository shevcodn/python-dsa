def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0

    for fast in range(slow, len(arr)):
        if arr[fast] != arr[slow]:
            slow = slow + 1
            arr[slow] = arr[slow] = arr[fast]

    return slow + 1

print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3]))
print(remove_duplicates([1]))