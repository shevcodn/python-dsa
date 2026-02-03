def count_lines(filename):
	with open("greeting.txt", "r") as file:
		lines = file.readlines()
		return len(lines)

result = count_lines("greeting.txt")
print(result)
