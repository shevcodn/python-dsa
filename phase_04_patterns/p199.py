def get_long_words(words, min_length):
	long = filter(lambda w: len(w) > min_length, words)
	upper = map(lambda w: w.upper(), long)
	return list(upper)

words = ["hi", "hello", "cat", "python", "ok"]
print(get_long_words(words, 3))
