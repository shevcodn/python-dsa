def unzip_lists(pairs):
	first = []
	second = []
	for pair in pairs:
		first.append(pair[0])
		second.append(pair[1])
	return [first, second]

print(unzip_lists([[1, 4], [2, 5], [3, 6]]))
print(unzip_lists([["a", "c"], ["b", "d"]]))
print(unzip_lists([[1, 2]]))

