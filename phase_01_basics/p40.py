def all_positive(n):
	for num in n:
		if num <= 0:
			return False
	return True

print(all_positive([1, 2, 3, 4]))
print(all_positive([1, -2, 3]))
print(all_positive([0, 1, 2])) 
