def find_word(filename, word):
	with open("greeting.txt", "r") as file:
		content = file.read()
		if word in content:
			return True
		else:
			return False

print(find_word("greeting.txt", "Python"))
print(find_word("greeting.txt", "Java"))
print(find_word("greeting.txt", "conding"))
