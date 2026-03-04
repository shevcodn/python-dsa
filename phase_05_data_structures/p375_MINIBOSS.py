from collections import Counter

def max_vowels(s, k):
    vowels = set('aeiou')
    count = sum(1 for i in range(k) if s[i] in vowels)
    result = count
    for i in range(k, len(s)):
        count += (s[i] in vowels)
        count -= (s[i - k] in vowels)
        result = max(result, count)
    return result

print(max_vowels("abciiidef", 3))
print(max_vowels("aeiou", 2))

def find_anagrams(s, p):
    p_count = Counter(p)
    s_count = Counter()
    result = []
    left = 0
    for right in range(len(s)):
        s_count[s[right]] += 1
        if right - left + 1 > len(p):
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1
        if s_count == p_count:
            result.append(left)
    return result

print(find_anagrams("cbaebabacd", "abc"))
print(find_anagrams("abab", "ab"))

def min_window_substring(s, t):
    t_count = Counter(t)
    s_count = Counter()
    left = 0
    min_length = float('inf')
    min_start = 0
    for right in range(len(s)):
        s_count[s[right]] += 1
        while all(s_count[c] >= t_count[c] for c in t_count):
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_start = left
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1
    return s[min_start:min_start + min_length] if min_length != float('inf') else ""

print(min_window_substring("ADOBECODEBANC", "ABC"))
print(min_window_substring("a", "a"))