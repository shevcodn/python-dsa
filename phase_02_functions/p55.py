def sum_until(n):
	total = 0
	for num in n:
		if num < 0:
			return total
		
		total = total + num
	return total

print(sum_until([1, 2, 3, -1, 5]))
print(sum_until([-1, 2, 3]))
print(sum_until([5, 10, 15]))
