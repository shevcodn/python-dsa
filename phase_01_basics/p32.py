def sum_even(n):
	total = 0
	for num in n:
		if num % 2 == 0:
			total = total + num
	return total

print(sum_even([1, 2, 3, 4, 5, 6]))
print(sum_even([1, 3, 5]))
print(sum_even([2, 4, 6]))
