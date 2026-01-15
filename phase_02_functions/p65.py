def word_lengths(text):
	words = text.split()
	result = []
	for word in words:
		result.append(len(word))
	return result

print(word_lengths("hi hello world"))
print(word_lengths("a bb cc"))
print(word_lengths("python"))

