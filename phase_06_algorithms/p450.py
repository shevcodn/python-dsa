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

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def find_range(arr, target):
    def find_first(arr, t):
        left, right, result = 0, len(arr)-1, -1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == t:
                result = mid
                right = mid-1
            elif arr[mid] < t:
                left = mid+1
            else:
                right = mid-1
        return result
    
    def find_last(arr, t):
        left, right, result = 0, len(arr)-1, -1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == t:
                result = mid
                left = mid+1
            elif arr[mid] < t:
                left = mid+1
            else:
                right = mid-1
        return result
    
    return [find_first(arr, target), find_last(arr, target)]

transactions = [
    {"id": 1, "amount": 500},
    {"id": 2, "amount": 1200},
    {"id": 3, "amount": 300},
    {"id": 4, "amount": 800},
]

def sort_transactions(txns):
    return sorted(txns, key=lambda x: x["amount"], reverse=True)

print(merge_sort([3,1,4,1,5,9,2,6]))
print(quick_sort([3,1,4,1,5,9,2,6]))
print(find_range([1,2,2,2,3,4], 2))
sorted_txns = sort_transactions(transactions)
for t in sorted_txns:
    print(f"${t['amount']}")
    
