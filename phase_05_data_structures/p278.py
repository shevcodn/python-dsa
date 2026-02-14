def first_unique(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
        
print(first_unique("leetcode"))
print(first_unique("aabb"))
print(first_unique("abcabc"))
print(first_unique("abcd"))
