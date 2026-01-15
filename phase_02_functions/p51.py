def double_evens(n):
	result = []
	for num in n:
		if num % 2 == 0:
			result.append(num * 2)
		else:
			result.append(num)
	return result

print(double_evens([1, 2, 3, 4]))
print(double_evens([5, 6, 7]))
print(double_evens([2, 4, 6]))
