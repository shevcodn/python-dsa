def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort_objects(items, key):
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and items[j][key] > current[key]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current
    return items

def sort_and_flag(transactions, threshold):
    sorted_tx = insertion_sort_objects(transactions, "amount")
    flagged = [tx for tx in sorted_tx if tx["amount"] > threshold]
    return sorted_tx, flagged

transactions = [
    {"id": "T1", "amount": 250.0, "user": "alice"},
    {"id": "T2", "amount": 12000.0, "user": "bob"},
    {"id": "T3", "amount": 80.0, "user": "carol"},
    {"id": "T4", "amount": 5500.0, "user": "dave"},
    {"id": "T5", "amount": 950.0, "user": "eve"},
]

print(insertion_sort([12, 11, 13, 5, 6]))
print(insertion_sort([4, 3, 2, 10, 12, 1, 5, 6]))

all_sorted, flagged = sort_and_flag(transactions, 1000)
print("Sorted transactions:")
for tx in all_sorted:
    print(f"  {tx['id']}: ${tx['amount']}")
print("Flagged (>$1000):", [tx["id"] for tx in flagged])
