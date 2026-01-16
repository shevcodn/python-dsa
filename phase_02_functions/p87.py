def count_occurrences_nested(n):
	counts = {}
	for sublist in n:
		for item in sublist:
			if item in counts:
				counts[item] = counts[item] + 1
			else:
				counts[item] = 1
	return counts

print(count_occurrences_nested([[1, 2], [1, 3]]))
print(count_occurrences_nested([["a", "a"], ["b"]]))
print(count_occurrences_nested([[1, 1, 1]]))

