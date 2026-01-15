def contains_all(n, count):
	for val in count:
		if val not in n:
			return False
	return True

print(contains_all([1, 2, 3, 4, 5], [2, 4]))
print(contains_all([1, 2, 3], [4, 5]))
print(contains_all(["a", "b", "c"], ["a", "c"]))
