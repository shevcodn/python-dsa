def sum_digits(n):
	total = 0
	for char in str(n):
		total = total + int(char)
	return total 

print(sum_digits(123))
print(sum_digits(9999))
print(sum_digits(5))
