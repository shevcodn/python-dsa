def average_nested(n):
	total = 0
	count = 0
	for sublist in n:
		for item in sublist:
			total = total + item
			count = count + 1
	return total / count

print(average_nested([[1, 2], [3, 4]]))
print(average_nested([[10, 20], [30]]))
print(average_nested([[5]])) 
