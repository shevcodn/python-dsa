def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def two_sum_all_pairs(nums, target):
    seen = {}
    pairs = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            for j in seen[complement]:
                pairs.append((j, i))
        if num not in seen:
            seen[num] = []
        seen[num].append(i)
    return pairs

def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))

print(two_sum_all_pairs([1, 2, 3, 2, 4, 1], 3))

payment_amounts = [-50, 20, -20, 30, -10, 10, 0]
print("Zero-sum payment groups:", three_sum(payment_amounts))

transfers = [100, 200, 300, 400, 500]
target_transfer = 600
print(f"Transactions summing to {target_transfer}: {two_sum(transfers, target_transfer)}")
