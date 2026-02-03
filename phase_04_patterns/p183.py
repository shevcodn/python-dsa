def replace_word(filename, old_word, new_word):
	with open("test.txt", "r") as file:
		content = file.read()

	content = content.replace(old_word, new_word)

	with open("test.txt", "w") as file:
		file.write(content)

replace_word("test.txt", "Python", "JavaScript")
