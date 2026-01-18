class Player:
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def add_points(self, points):
		self.score = self.score + points

	def get_info(self):
		return f"Name : {self.name}, Score: {self.score}"

p1 = Player("Denis", 0)
p2 = Player("Alex", 10)

p1.add_points(5)
p1.add_points(3)
p2.add_points(7)

print(p1.get_info())
print(p2.get_info())
