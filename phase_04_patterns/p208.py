def even_numbers(n):
	i = 0
	while i <= n:
		if i % 2 == 0:
			yield i
		i += 1

for num in even_numbers(10):
	print(num)
