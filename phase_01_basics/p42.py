def find_min(n):
	smallest = n[0]
	for num in n:
		if num <= smallest:
			smallest = num 
	return smallest

print(find_min([1, 5, 3, 9 ,2]))
print(find_min([10, 2, 3]))
print(find_min([-5, -2, -10]))
