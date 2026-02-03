def process_number(x):
	try:
		num = int(x)
	except ValueError:
		return "Invalid input"
	else:
		return num * 2

print(process_number("10"))
print(process_number("abc"))
print(process_number("5"))
