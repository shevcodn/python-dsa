def count_in_nested(n, value):
	count = 0
	for sublist in n:
		for item in sublist:
			if item == value:
				count = count + 1
	return count

print(count_in_nested([[1, 2, 1], [1, 3]], 1))
print(count_in_nested([[1, 2], [3, 4]], 5))
print(count_in_nested([["a", "a"], ["a", "b"]], "a"))

