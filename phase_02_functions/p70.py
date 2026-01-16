def second_largest(n):
	unique = list(set(n))
	unique.sort()
	return unique[-2]

print(second_largest([1, 5, 3, 9, 2]))
print(second_largest([10, 10, 5]))
