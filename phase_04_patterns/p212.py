def countdown(n):
	while n > 0:
		yield n
		n -= 1

ct = countdown
for num in ct(5):
	print(num)
