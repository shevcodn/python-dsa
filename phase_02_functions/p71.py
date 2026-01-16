def flatten(n):
	result = []
	for sublist in n:
		for item in sublist:
			result.append(item)
	return result

print(flatten([[1, 2], [3, 4], [5]]))
print(flatten([["a", "b"], ["c"]]))
print(flatten([[1], [2], [3]]))
