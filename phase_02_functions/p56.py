def multiply_until(n):
	total = 1
	for num in n:
		if num == 0:
			return total

		total = total * num
	return total

print(multiply_until([2, 3, 4, 0, 5]))
print(multiply_until([0, 2, 3]))
print(multiply_until([5, 2, 3]))
