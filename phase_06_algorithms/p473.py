from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""
    
    need = Counter(t)
    have = {}
    formed = 0
    required = len(need)

    left = 0
    min_left = float('inf')
    result = ""

    for right in range(len(s)):
        char = s[right]
        have[char] = have.get(char, 0) + 1

        if char in need and have[char] == need[char]:
            formed += 1

        while formed == required:
            if right - left + 1 < min_left:
                min_left = right - left + 1
                result = s[left : right + 1]

            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return result


print(min_window("ADOBECODEBANC", "ABC"))
print(min_window("a", "a"))
print(min_window("a", "b"))
print(min_window("aa", "aa"))