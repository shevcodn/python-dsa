def count_word(filename, word):
	with open("test.txt", "r") as file:
		content = file.read()
		return content.count(word)

print(count_word("test.txt", "is"))
print(count_word("test.txt", "Python"))
print(count_word("test.txt", "Java"))
