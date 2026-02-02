class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

p1 = Point(5, 10)
p2 = Point(5, 10)
p3 = Point(3, 7)

print(p1 == p2)
print(p2 == p3)

