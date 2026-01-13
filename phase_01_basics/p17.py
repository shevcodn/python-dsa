def contains(items, target):
	if target in items:
		return True
	else:
		return False

print(contains([1, 2, 3], 2))
print(contains([1, 2, 3], 5))
