def read_file(filename):
	with open("greeting.txt", "r") as file:
		content = file.read()
		return content

content = read_file("greeting.txt")
print(content)
