def get_unique_nested(n):
	result = []
	for sublist in n:
		for item in sublist:
			if item not in result:
				result.append(item)
	return result

print(get_unique_nested([[1, 2], [2, 3]]))
print(get_unique_nested([[1, 1], [1, 1]]))
print(get_unique_nested([["a", "b"], ["b", "c"]]))

