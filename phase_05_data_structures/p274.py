def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 1, 2, 3, 4, 4]))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([1, 2, 3]))
