def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def rank_accounts(balances):
    indexed = list(enumerate(balances))
    n = len(indexed)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if indexed[j][1] > indexed[max_idx][1]:
                max_idx = j
        indexed[i], indexed[max_idx] = indexed[max_idx], indexed[i]
    return [(f"Account #{idx}", balance) for idx, balance in indexed]

print(selection_sort([64, 25, 12, 22, 11]))
print(selection_sort([9, 1, 8, 2, 7, 3]))
print(selection_sort_desc([3, 1, 4, 1, 5, 9, 2, 6]))

balances = [15000, 4200, 87000, 320, 51000]
for name, balance in rank_accounts(balances):
    print(f"{name}: ${balance:,}")
