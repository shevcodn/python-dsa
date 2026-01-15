def ends_with(n, letter):
	result = []
	for word in n:
		if word[-1] == letter:
			result.append(word)
	return result

print(ends_with(["hello", "world", "go"], "o"))
print(ends_with(["cat", "dog", "bird"], "d"))
print(ends_with(["abc", "def"], "x"))
