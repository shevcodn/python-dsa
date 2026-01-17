def chunk_list(items, size):
	result = []
	for i in range(0, len(items), size):
		chunk = items[i:i+size]
		result.append(chunk)
	return result

print(chunk_list([1, 2, 3, 4, 5, 6], 2))
print(chunk_list([1, 2, 3, 4, 5], 2))
print(chunk_list([1, 2, 3], 3))
