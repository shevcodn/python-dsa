def get_odds(n):
	result = []
	for num in n:
		if num % 2 != 0:
			result.append(num)
	return result

print(get_odds([1, 2, 3, 4, 5, 6]))
print(get_odds([2, 4, 6]))
print(get_odds([1, 3, 5]))
