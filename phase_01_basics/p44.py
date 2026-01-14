def reverse_list(n):
	result = []
	for num in n:
		result = [num] + result
	return result

print(reverse_list([1, 2, 3]))
print(reverse_list(["a", "b", "c"]))
print(reverse_list([5]))
