def count_nested(n):
	total = 0
	for sublist in n:
		for num in sublist:
			total += 1
	return total

print(count_nested([[1, 2], [3, 4], [5]]))
print(count_nested([[1], [2], [3]]))
print(count_nested([["a", "b"], ["c", "d", "e"]]))

