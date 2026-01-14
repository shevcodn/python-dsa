def replace_value(n, old, new):
	result = []
	for num in n:
		if num == old:
			result.append(new)
		else:
			result.append(num)
	return result

print(replace_value([1, 2, 3, 2], 2, 9))
print(replace_value(["a", "b", "a"], "a", "x"))
print(replace_value([1, 1, 1], 1, 0))
