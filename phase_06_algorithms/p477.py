from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)

    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))

