def square_all(numbers):
	result = []
	for num in numbers:
		result.append(num ** 2)
	return result

print(square_all([1, 2, 3]))
print(square_all([4, 5]))
