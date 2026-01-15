def starts_with(n, letter):
	result = []
	for word in n:
		if word[0] == letter:
			result.append(word)
	return result

print(starts_with(["apple", "banana", "apricot"], "a"))
print(starts_with(["cat", "dog", "cow"], "c"))
print(starts_with(["hi", "hello", "bye"], "x"))
