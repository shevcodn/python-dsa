def count_positive(n):
	count = 0
	for num in n:
		if num > 0:
			count = count + 1
	return count

print(count_positive([1, -2, 3, -4, 5]))
print(count_positive([-1, -2, -3]))
print(count_positive([5, 10, 15]))
