def count_words(text):
	words = text.split()
	return len(words)

print(count_words("hello world"))
print(count_words("one tho three four"))
print(count_words("hi"))
