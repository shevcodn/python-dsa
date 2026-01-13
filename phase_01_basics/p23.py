def clamp(n, min_val, max_val):
	if n < min_val:
		return min_val
	elif n > max_val:
		return max_val
	else:
		return n


print(clamp(5, 1, 10))
print(clamp(15, 1, 10))
print(clamp(-5, 1, 10))
