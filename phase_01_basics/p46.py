def index_of(n, value):
	index = 0
	for num in n:
		if num == value:
         		return index
		index = index + 1
	return -1

print(index_of([10, 20, 30], 20))
print(index_of(["a", "b", "c"], "c"))
print(index_of([1, 2, 3, 4, 5], 5))
