def can_sum(nums, target):
    if target == 0:
        return True
    if target < 0:
        return False
    
    for num in nums:
        remainder = target - num
        if can_sum(nums, remainder):
            return True
    return False
    
print(can_sum([2,3,7], 7))
print(can_sum([2,4], 7))


def min_platforms(arrivals, departures):
    if not arrivals or not departures or len(arrivals) != len(departures):
        return 0
    
    arrivals.sort()
    departures.sort()

    platform_needed = 0
    max_platforms = 0
    i = j = 0

    while i < len(arrivals) and j < len(departures):
        if arrivals[i] < departures[j]:
            platform_needed += 1
            max_platforms = max(max_platforms, platform_needed)
            i += 1
        else:
            platform_needed -= 1
            j += 1

    return max_platforms

print(min_platforms([900,940,950], [910,1200,1120]))


def longest_k_unique(s, k):
    if k == 0:
        return 0
    
    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_k_unique("araaci", 2))