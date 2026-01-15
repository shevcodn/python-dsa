def longest_word(text):
	words = text.split()
	longest = ""
	for word in words:
		if len(word) > len(longest):
			longest = word
	return longest

print(longest_word("hi hello world"))
print(longest_word("cat elephant dog"))
print(longest_word("a bb ccc"))
