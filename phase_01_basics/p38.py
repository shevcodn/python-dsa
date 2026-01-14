def sum_positive(n):
	total = 0
	for num in n:
		if num > 0:
			total += num
	return total


print(sum_positive([1, -2, 3, -4, 5]))
print(sum_positive([-1, -2, -3,]))
print(sum_positive([5, 10, 15]))

