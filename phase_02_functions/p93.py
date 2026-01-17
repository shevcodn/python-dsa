def merge_sorted(a, b):
	result = a + b
	return sorted(result)

print(merge_sorted([1, 3, 5], [2, 4, 6]))
print(merge_sorted([1, 2], [3, 4, 5]))
print(merge_sorted([], [1, 2]))
