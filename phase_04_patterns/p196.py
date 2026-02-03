def square_evens(numbers):
	return [x**2 for x in numbers if x % 2 == 0]

print(square_evens([1, 2, 3, 4, 5, 6]))
print(square_evens([1, 3, 5]))
print(square_evens([2, 4, 8]))
