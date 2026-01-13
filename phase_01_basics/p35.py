def count_letter(text, letter):
	count = 0
	for char in text:
		if char == letter:
			count = count + 1
	return count

print(count_letter("banana", "a"))
print(count_letter("hello", "l"))
print(count_letter("hello", "x"))
