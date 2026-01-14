def find_max(n):
	biggest = n[0]
	for num in n:
		if num > biggest:
				biggest = num
	return biggest

print(find_max([1, 5, 3, 9, 2]))
print(find_max([10, 2, 3,]))
print(find_max([-5, -2, -10])) 
