def multiply_all_nested(n):
	total = 1
	for sublist in n:
		for item in sublist:
			total = total * item
	return total

print(multiply_all_nested([[1, 2], [3, 4]]))
print(multiply_all_nested([[2, 3], [4]]))
print(multiply_all_nested([[5], [2]]))
 
