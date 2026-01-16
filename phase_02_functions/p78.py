def get_all_even_nested(n):
	result = []
	for sublist in n:
		for item in sublist:
			if item % 2 == 0:
				result.append(item)
	return result

print(get_all_even_nested([[1, 2], [3, 4]]))
print(get_all_even_nested([[1, 3], [5, 7]]))
print(get_all_even_nested([[2, 4], [6, 8]]))

