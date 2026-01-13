def count_char(text, char):
	count = 0
	for letter in text:
		if letter == char:
			count += 1
	return count

print(count_char("hello", "l"))
print(count_char("banana", "a"))
