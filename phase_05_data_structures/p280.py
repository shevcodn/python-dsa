def longest_common_prefix(words):
    if not words:
        return ""
    
    prefix = words[0]
    for word in words[1:]:
        while word[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["interview", "inter", "internal"]))