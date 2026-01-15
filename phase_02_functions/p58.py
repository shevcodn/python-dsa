def remove_short(n, min_len):
	result = []
	for word in n:
		if len(word) >= min_len:
				result.append(word)
	return result

print(remove_short(["hi", "hello", "a", "world"], 3))
print(remove_short(["cat", "dog", "rat"], 3))
print(remove_short(["a", "bb", "ccc"], 2)) 
