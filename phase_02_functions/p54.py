def first_greater(n, value):
	for num in n:
		if num > value:
			return num
	return None

print(first_greater([1, 5, 3, 9], 4))
print(first_greater([1, 2, 3], 10))
print(first_greater([10, 20, 30], 5))
