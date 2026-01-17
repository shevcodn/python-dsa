def zip_lists(a, b):
	result = []
	for i in range(len(a)):
		pair = [a[i], b[i]]
		result.append(pair)
	return result

print(zip_lists([1, 2, 3], [4, 5, 6]))
print(zip_lists(["a", "b"], ["c", "d"]))
print(zip_lists([1], [2]))
