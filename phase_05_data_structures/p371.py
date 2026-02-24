from collections import defaultdict

def longest_subarray(nums, k):
    window = defaultdict(int)
    left = 0
    result = 0
    for right in range(len(nums)):
        window[nums[right]] += 1
        while len(window) > k:
            window[nums[left]] -= 1
            if window[nums[left]] == 0:
                del window[nums[left]]
            left += 1
        result = max(result, right - left + 1)
    return result


print(longest_subarray([1,2,1,2,3], 2))
print(longest_subarray([1,2,1,3,4], 2))

