class Player:
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def __lt__(self, other):
		return self.score < other.score

	def __gt__(self, other):
		return self.score > other.score

p1 = Player("Denis", 100)
p2 = Player("Ivan", 150)

print(p1 < p2)
print(p1 > p2)
print(p2 > p1)
