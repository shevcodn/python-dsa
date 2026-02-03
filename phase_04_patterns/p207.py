def squares(n):
	i = 1
	while i <= n:
		yield i * i
		i += 1

for num in squares(5):
	print(num)
