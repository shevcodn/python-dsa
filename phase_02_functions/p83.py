def has_negative_nested(n):
	for sublist in n:
		for item in sublist:
			if item < 0:
				return True
	return False


print(has_negative_nested([[1, 2], [3, 4]]))
print(has_negative_nested([[1, -2], [3, 4]]))
print(has_negative_nested([[-1], [-2]]))
