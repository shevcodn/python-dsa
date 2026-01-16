def all_positive_nested(n):
	for sublist in n:
		for item in sublist:
			if item <= 0:
				return False
	return True

print(all_positive_nested([[1, 2], [3, 4]]))
print(all_positive_nested([[1, -2], [3, 4]]))
print(all_positive_nested([[0, 1], [2]]))
