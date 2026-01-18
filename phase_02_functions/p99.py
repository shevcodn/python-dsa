def second_most_common(items):
	best = items[0]
	best_count = items.count(items[0])
	second = None
	second_count = 0
	
	for item in items:
		count = items.count(item)
		if count > best_count:
			second = best
			second_count = best_count
			best = item
			best_count = count
		elif count > second_count and item != best:
			second = item
			second_count = count
	return second


print(second_most_common([1, 1, 1, 2, 2, 3]))
print(second_most_common(["a", "a", "b", "b", "b", "c"]))
print(second_most_common([5, 5, 5, 5, 1, 1, 1]))
