from collections import Counter

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(t) == Counter(s)

def is_anagram_v2(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        count[char] = count.get(char, 0) - 1
        if count[char] < 0:
            return False
    return True
    
print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram_v2("anagram", "nagaram"))
print(is_anagram_v2("rat", "car"))