def get_evens(n):
	result = []
	for num in n:
		if num % 2 == 0:
			result.append(num)
	return result

print(get_evens([1, 2, 3, 4, 5, 6]))
print(get_evens([1, 3, 5]))
print(get_evens([2, 4, 6]))
