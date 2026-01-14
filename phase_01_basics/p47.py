def count_greater(n, value):
	count = 0
	for num in n:
		if num > value:
			count = count + 1
	return count

print(count_greater([1, 5, 10, 3], 4))
print(count_greater([1, 2, 3], 10))
print(count_greater([5, 5, 5], 4))
