def even_numbers(n):
	i = 0
	while i <= n:
		yield i
		i += 2

for num in even_numbers(10):
	print(num)
