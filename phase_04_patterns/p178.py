def append_to_file(filename, text):
	with open("greeting.txt", "a") as file:
		file.write(text + "\n")
