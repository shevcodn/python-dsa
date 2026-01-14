def remove_value(n, value):
	result = []
	for num in n:
		if num != value:
			result.append(num)
	return result

print(remove_value([1, 2, 3, 2, 4], 2))
print(remove_value(["a", "b", "a"], "a"))
print(remove_value([1, 1, 1], 1))
