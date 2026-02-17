def length_of_longest(s):
    seen = {}
    left = 0
    llongest = 0
    for right, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1
        seen[c] = right
        llongest = max(llongest, right - left + 1)
    return llongest


print(length_of_longest("abcabcbb"))
print(length_of_longest("bbbbb"))
print(length_of_longest("dvdf"))