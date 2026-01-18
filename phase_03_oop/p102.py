class Counter:
	def __init__(self):
		self.count = 0

	def increment(self):
		self.count = self.count + 1

	def get_count(self):
		f"Count : {self.count}"
		return self.count

c = Counter()
print(c.get_count())
c.increment()
c.increment()
c.increment()
print(c.get_count())
