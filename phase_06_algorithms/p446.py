def first_unique(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for i, char in enumerate(s):
        if count[char] == 1:
            return i
        
    return -1

print(first_unique("leetcode"))
print(first_unique("loveleet"))
print(first_unique("aabb"))
