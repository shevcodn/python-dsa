def find_duplicates(items):
	result = []
	for item in items:
		if items.count(item) > 1:
			if item not in result:
				result.append(item)
	return result

print(find_duplicates([1, 2, 2, 3, 3, 3]))
print(find_duplicates([1, 2, 3]))
print(find_duplicates([1, 1, 1, 1]))
