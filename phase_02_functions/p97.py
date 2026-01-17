def group_by_length(words):
	groups = {}
	for word in words:
		length = len(word)
		if length in groups:
			groups[length].append(word)
		else:
			groups[length] = [word]
	return groups


print(group_by_length(["hi", "hey", "hello", "yo"]))
print(group_by_length(["a", "bb", "ccc"]))
