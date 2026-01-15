def square_evens(n):
	result = []
	for num in n:
		if num % 2 == 0:
			result.append(num ** 2)
		else:
			result.append(num)
	return result

print(square_evens([1, 2, 3, 4]))
print(square_evens([5, 6]))
print(square_evens([2, 3, 4]))
