def contains_duplicate(nums):
    return len(nums) != len(set(nums))

def contains_nearby_duplicate(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False

def find_duplicate_within_window(nums, k, threshold):
    for i in range(len(nums)):
        window = nums[i:i + k + 1]
        window_sorted = sorted(window)
        for j in range(len(window_sorted) - 1):
            if abs(window_sorted[j + 1] - window_sorted[j]) <= threshold:
                return True
    return False

def count_unique(items):
    return len(set(items))

print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

print(contains_nearby_duplicate([1, 2, 3, 1], 3))
print(contains_nearby_duplicate([1, 0, 1, 1], 1))
print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2))

tx_amounts = [250.0, 300.0, 250.0, 400.0, 250.0]
print(f"Duplicate amounts: {contains_duplicate(tx_amounts)}")
print(f"Same amount within 2 transactions: {contains_nearby_duplicate(tx_amounts, 2)}")

prices = [1.0, 1.001, 1.003, 1.0, 1.002]
print(f"Suspicious price similarity within window: {find_duplicate_within_window(prices, 3, 0.005)}")

user_ids = ["u1", "u2", "u3", "u2", "u4", "u1"]
print(f"Unique active users: {count_unique(user_ids)}")
