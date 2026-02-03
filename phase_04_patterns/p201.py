def find_longest(*words):
	longest = words[0]
	for word in words:
		if len(word) > len(longest):
			longest = word
	return longest

print(find_longest("hi", "hello", "cat"))
print(find_longest("a", "bb", "ccc"))
