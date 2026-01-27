class Counter:
	def __init__(self):
		self.count = 0

	def click(self):
		self.count = self.count + 1

	def get_count(self):
		return self.count

	def reset(self):
		self.count = 0
		return self.count

c = Counter()
c.click()
c.click()
c.click()
print(c.get_count())
c.reset()
print(c.get_count())

