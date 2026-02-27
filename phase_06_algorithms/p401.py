def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def bubble_sort_by_key(records, key):
    n = len(records)
    for i in range(n):
        for j in range(n - i - 1):
            if records[j][key] > records[j + 1][key]:
                records[j], records[j + 1] = records[j + 1], records[j]
    return records

transactions = [
    {"id": "T003", "amount": 4500.00, "currency": "CAD"},
    {"id": "T001", "amount": 120.50, "currency": "CAD"},
    {"id": "T005", "amount": 9800.00, "currency": "CAD"},
    {"id": "T002", "amount": 250.75, "currency": "CAD"},
    {"id": "T004", "amount": 670.00, "currency": "CAD"},
]

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([1]))
print(bubble_sort([]))

sorted_tx = bubble_sort_by_key(transactions, "amount")
for tx in sorted_tx:
    print(f"{tx['id']}: ${tx['amount']}")
