def max_in_nested(n):
	best = n[0][0]
	for sublist in n:
		for item in sublist:
			if item > best:
				best = item
	return best

print(max_in_nested([[1, 2], [3, 4]]))
print(max_in_nested([[10, 5], [3, 8]]))
print(max_in_nested([[-1, -5], [-2]]))

