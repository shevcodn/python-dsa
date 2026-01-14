def average(n):
	total = 0
	for num in n:
		total = total + num
	return total / len(n)

print(average([1, 2, 3, 4, 5]))
print(average([10, 20]))
print(average([7]))
