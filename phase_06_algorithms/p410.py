def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

def find_all_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

def find_duplicate_floyd(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

def find_missing_and_duplicate(nums):
    n = len(nums)
    seen = set()
    duplicate = -1
    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)
    expected = set(range(1, n + 1))
    missing = list(expected - seen)[0]
    return duplicate, missing

print(find_duplicate([1, 3, 4, 2, 2]))
print(find_duplicate([3, 1, 3, 4, 2]))

print(find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))

print(find_duplicate_floyd([3, 1, 3, 4, 2]))

tx_ids = [101, 102, 103, 104, 102, 105, 103]
dup = find_all_duplicates(tx_ids)
print(f"Duplicate transaction IDs detected: {dup}")

records = [1, 2, 4, 4, 5]
dup, missing = find_missing_and_duplicate(records)
print(f"Duplicate: {dup}, Missing: {missing}")
