def count_occurrences(lst, target):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_occurrences(item, target)
        elif item == target:
            count += 1
    return count
      
print(count_occurrences([1, 2, 1, [1, 3, [1, 2]]], 1))
print(count_occurrences([1, 2, 3], 5))
print(count_occurrences([[1], [1], [1]], 1))