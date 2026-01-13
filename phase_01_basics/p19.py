def remove_negative(numbers):
	result = []
	for num in numbers:
		if num > 0:
			result.append(num)
	return result

print(remove_negative([1, -2, 3, -4, 5]))
print(remove_negative([-1, -2, -3]))
