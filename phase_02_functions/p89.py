def reverse_nested(n):
	result = []
	for sublist in n:
		result.append(n)
	return result

print(reverse_nested([[1, 2, 3], [4, 5]]))
print(reverse_nested([["a", "b"], ["c", "d", "e"]]))
print(reverse_nested([[1], [2]]))

