def count_even(n):
	count = 0
	for number in n:
		count = count + 1
	return count

print(count_even([1, 2, 3, 4, 5, 6]))
print(count_even([1, 3, 5]))
print(count_even([2, 4, 6]))
