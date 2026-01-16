def sum_if_positive_nested(n):
	count = 0
	for num in n:
		for item in num:
			if item > 0:
				count = count + item
	return count

print(sum_if_positive_nested([[1, -2], [3, -4]]))
print(sum_if_positive_nested([[-1, -2], [-3]]))
print(sum_if_positive_nested([[5, 5], [5]]))

