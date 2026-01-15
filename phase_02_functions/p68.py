def is_palindrome_number(n):
	text = str(n)
	if text == text[::-1]:
		return True
	return False

print(is_palindrome_number(121))
print(is_palindrome_number(123))
print(is_palindrome_number(1221))
