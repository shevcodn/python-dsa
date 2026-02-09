def square_gen(n):
	return (x**2 for x in range(n+1))

gen = square_gen(5)
print(list(gen))
