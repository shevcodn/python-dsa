def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]

def merge_sort_key(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_key(arr[:mid], key)
    right = merge_sort_key(arr[mid:], key)
    return merge_by_key(left, right, key)

def merge_by_key(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
print(merge_sort([1]))
print(merge_sort([5, 4, 3, 2, 1]))

portfolio = [
    {"ticker": "AAPL", "gain_pct": 12.4},
    {"ticker": "TSLA", "gain_pct": -8.2},
    {"ticker": "MSFT", "gain_pct": 22.1},
    {"ticker": "AMZN", "gain_pct": 5.7},
    {"ticker": "NVDA", "gain_pct": 41.3},
]

sorted_portfolio = merge_sort_key(portfolio, "gain_pct")
print("Portfolio by performance:")
for stock in sorted_portfolio:
    print(f"  {stock['ticker']}: {stock['gain_pct']:+.1f}%")
