def index_in_nested(n, value):
	for i in range(len(n)):
		for j in range(len(n[i])):
			if n[i][j] == value:
				return (i, j)
	return None

print(index_in_nested([[1, 2], [3, 4]], 3))
print(index_in_nested([[1, 2], [3, 4]], 5))
print(index_in_nested([["a", "b"], ["c"]], "b"))
