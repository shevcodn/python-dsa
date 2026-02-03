def write_greeting(name, filename):
	with open(filename, "w") as file:
		file.write(f"Hello, {name}!")

write_greeting("Denis", "greeting.txt")
