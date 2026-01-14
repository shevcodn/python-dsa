def multiply_all(n):
	total = 1
	for num in n:
		total = total * num
	return total

print(multiply_all([1, 2, 3, 4]))
print(multiply_all([2, 5]))
print(multiply_all([7]))
