def count_vowels(text):

	vowels = "aeiou"
	count = 0
	for char in vowels:
		count += 1
	return count

print(count_vowels("Hello"))
print(count_vowels("Python"))
