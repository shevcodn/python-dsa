def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
