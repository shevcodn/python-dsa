def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = arr[i]
    return arr

print(insertion_sort([5, 3, 1, 4, 2]))
print(insertion_sort([9, 1, 8, 2, 7]))