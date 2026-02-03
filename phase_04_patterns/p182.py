def copy_file(source, destination):
	with open("test.txt", "r") as file:
		content = file.read()

	with open("destination", "w") as file:
		file.write(content)

copy_file("test.txt", "backup.txt")
