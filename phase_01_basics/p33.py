def first_even(n):
	for num in n:
		if num % 2 == 0:
			return num
	return None

print(first_even([1, 3, 4, 5, 6]))
print(first_even([1, 3, 5]))
print(first_even([2, 4, 6]))
