def longest_unique(s):
    window = {}
    left = 0
    result = 0
    for right in range(len(s)):
        if s[right] in window:
            left = max(left, window[s[right]] + 1)
        window[s[right]] = right
        result = max(result, right - left + 1)
    return result

print(longest_unique("abcabcbb"))
print(longest_unique("bbbbb"))
print(longest_unique("pwwkew"))