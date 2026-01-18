class LimitedCounter:
	def __init__(self, max_value):
		self.count = 0
		self.max_value = max_value

	def increment(self):
		if self.count < self.max_value: 
			self.count = self.count + 1
	def get(self):
		return self.count

c = LimitedCounter(3)
print(c.get())

c.increment()
print(c.get())

c.increment()
print(c.get())

c.increment()
print(c.get())

c.increment()
print(c.get())

c.increment()
print(c.get())


