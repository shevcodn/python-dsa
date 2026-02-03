def sort_by_length(words):
	return sorted(words, key=lambda word: len(word))

words = ["apple", "hi", "banana", "cat"]
print(sort_by_length(words))


