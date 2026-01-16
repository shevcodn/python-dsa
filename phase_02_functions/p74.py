def find_in_nested(n, value):
	for sublist in n:
		for item in sublist:
			if item == value:
				return True
	return False

print(find_in_nested([[1, 2], [3, 4]], 3))
print(find_in_nested([[1, 2], [3, 4]], 5))
print(find_in_nested([["a", "b"], ["c"]], "c"))

