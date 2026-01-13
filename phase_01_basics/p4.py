def find_max(numbers):
	biggest = numbers[0]
	for num in numbers:
		if num > biggest:
			biggest = num
	return biggest

print(find_max([50, 60, 90 , 95]))
