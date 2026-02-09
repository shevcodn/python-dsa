def fibonacci(n):
	a, b = 0, 1
	count = 0
	while count < n:
		yield a
		a, b = b, a + b
		count += 1

fb = fibonacci
for num in fb(8):
	print(num)
