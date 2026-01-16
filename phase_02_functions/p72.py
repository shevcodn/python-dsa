def sum_nested(n):
	total = 0
	for sublist in n:
		for num in sublist:
			total += num
	return total

print(sum_nested([[1, 2], [3, 4], [5]]))
print(sum_nested([[10], [20], [30]]))
print(sum_nested([[1, 1, 1,], [2, 2]]))
