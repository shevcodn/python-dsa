def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_key(arr, key, reverse=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][key]
    left = [x for x in arr if x[key] < pivot]
    middle = [x for x in arr if x[key] == pivot]
    right = [x for x in arr if x[key] > pivot]
    result = quick_sort_key(left, key) + middle + quick_sort_key(right, key)
    return result[::-1] if reverse else result

def kth_largest(arr, k):
    sorted_arr = quick_sort(arr)
    return sorted_arr[-k]

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))
print(quick_sort([10, 7, 8, 9, 1, 5]))

prices = [
    {"symbol": "EUR/USD", "spread": 0.8},
    {"symbol": "GBP/USD", "spread": 1.2},
    {"symbol": "USD/JPY", "spread": 0.5},
    {"symbol": "AUD/USD", "spread": 1.8},
    {"symbol": "USD/CAD", "spread": 1.0},
]

print("Pairs sorted by spread (best first):")
for p in quick_sort_key(prices, "spread"):
    print(f"  {p['symbol']}: {p['spread']} pip")

daily_returns = [3.2, -1.5, 8.7, 0.3, -4.1, 12.0, 2.1]
print(f"3rd largest return: {kth_largest(daily_returns, 3)}%")
print(f"Best day: {kth_largest(daily_returns, 1)}%")
