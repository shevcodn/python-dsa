def has_negative(n):
	for num in n:
		if num < 0:
			return True
		
	return False

print(has_negative([1, 2, -3, 4]))
print(has_negative([1, 2, 3, 4]))
print(has_negative([-1]))
