def safe_divide(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(7, 2))
