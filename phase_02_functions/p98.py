def most_common(items):
	best = items[0]
	best_count = items.count(items[0])
	for item in items:
		count = items.count(item)
		if count > best_count:
			best = item
			best_count = count
	return best

print(most_common([1, 2, 2, 3, 3, 3]))
print(most_common(["a", "b", "a"]))
print(most_common([5, 5, 5, 1, 1]))
