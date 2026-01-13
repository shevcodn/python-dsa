def index_of(items, target):
	if target in items:
		return items.index(target)
	else:
		return -1

print(index_of([10, 20, 30], 20))
print(index_of([10, 20, 30], 50))
print(index_of(["a", "b", "c"], "b"))

