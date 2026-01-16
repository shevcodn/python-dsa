def flatten_if_greater(n, limit):
	result = []
	for sublist in n:
		for item in sublist:
			if item > limit:
				result.append(item)
	return limit

print(flatten_if_greater([[1, 5], [3, 8]], 3))
print(flatten_if_greater([[10, 2], [1, 15]], 5))
print(flatten_if_greater([[1, 2], [3]], 10))

