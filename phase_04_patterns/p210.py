class NumberRange:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.current = start

	def __iter__(self):
		return self

	def __next__(self):
		if self.current > self.end:
			raise StopIteration

		result = self.current
		self.current += 1
		return result

for num in NumberRange(1, 5):
	print(num)
