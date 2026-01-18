class Score:
	def __init__(self):
		self.points = 0

	def add(self, amount):
		self.points = self.points + amount

	def subtract(self, amount):
		self.points = self.points - amount
		if self.points < 0:
			self.points = 0

	def get(self):
		return self.points

s = Score()
print(s.get())

s.add(10)
print(s.get())

s.add(5)
print(s.get())

s.subtract(3)
print(s.get())

s.subtract(100)
print(s.get())
