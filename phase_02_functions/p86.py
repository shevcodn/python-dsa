def replace_in_nested(n, old, new):
	result = []
	for sublist in n:
		subresult = []
		for item in sublist:
			if item == old:
				subresult.append(new)
			else:
				subresult.append(item)
		result.append(subresult)
	return result

print(replace_in_nested([[1, 2], [2, 3]], 2, 9))
print(replace_in_nested([[1, 1], [1, 1]], 1, 0))
print(replace_in_nested([["a", "b"], ["c"]], "a", "x"))

