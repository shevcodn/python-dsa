def is_palindrome(text):
	if text == text[::-1]:
		return True
	else:
		return False

print(is_palindrome("radar"))
print(is_palindrome("hello"))
print(is_palindrome("level"))
