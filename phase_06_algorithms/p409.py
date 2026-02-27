def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def reverse_range(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    reverse_range(arr, 0, n - 1)
    reverse_range(arr, 0, k - 1)
    reverse_range(arr, k, n - 1)
    return arr

def rotate_left(arr, k):
    n = len(arr)
    k = k % n
    reverse_range(arr, 0, k - 1)
    reverse_range(arr, k, n - 1)
    reverse_range(arr, 0, n - 1)
    return arr

print(reverse_array([1, 2, 3, 4, 5]))
print(reverse_array([1, 2]))
print(reverse_array([1]))

print(rotate_right([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate_left([1, 2, 3, 4, 5, 6, 7], 2))

candles = [1.0820, 1.0835, 1.0812, 1.0850, 1.0798, 1.0866, 1.0844]
print("Latest 3 prices (newest first):", reverse_array(candles[:3]))
print("Shifted window by 2:", rotate_right(candles[:], 2))
