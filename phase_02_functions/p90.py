def sum_by_index_nested(n):
	result = []
	for i in range(len(n[0])):
		total = 0
		for sublist in n:
			total = total + sublist[i]
		result.append(total)
	return result

print(sum_by_index_nested([[1, 2], [3, 4]]))
print(sum_by_index_nested([[1, 2, 3], [4, 5, 6]]))
print(sum_by_index_nested([[10], [20], [30]]))

