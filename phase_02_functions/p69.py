def remove_duplicates_ordered(n):
	result = []
	for num in n:
		if num not in result:
			result.append(num)
	return result

print(remove_duplicates_ordered([1, 2, 2, 3, 1]))
print(remove_duplicates_ordered(["a", "b", "a", "c"]))
print(remove_duplicates_ordered([5, 5, 5]))
