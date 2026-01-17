def rotate_list(items, n):
	return items[n:] + items[:n]

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3], 1))
print(rotate_list([1, 2, 3, 4], 0))
