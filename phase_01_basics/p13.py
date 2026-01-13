def get_initials(name):
	result = ""
	words = name.split()
	for word in words:
		result += word[0]
	return result

print(get_initials("Denis Shevchenko"))
print(get_initials("John Paul Jones"))
