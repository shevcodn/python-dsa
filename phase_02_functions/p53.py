def keep_long(n, min):
	result = []
	for word in n:
		if len(word) > min:
			result.append(word)
	return result

print(keep_long(["hi", "hello", "a", "world"], 2))
print(keep_long(["cat", "dog", "elephant"], 3))
print(keep_long(["a", "b", "c"], 1))
