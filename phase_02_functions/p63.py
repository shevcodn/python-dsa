def shortest_word(text):
	words = text.split()
	shortest = words[0]
	for word in words:
		if len(word) < len(shortest):
			shortest = word
	return shortest

print(shortest_word("hi hello world"))
print(shortest_word("cat elephant dog"))
print(shortest_word("a bb ccc"))
