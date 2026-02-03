def safe_open_file(filename):
	try:
		with open(filename, "r") as file:
			return file.read()
	except FileNotFoundError:
		return "File not found"
	finally:
		print("Attempted to open file")

print(safe_open_file("test.txt"))
print(safe_open_file("missing.txt"))
