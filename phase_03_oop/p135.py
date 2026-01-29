class Shape:
	def area(self):
		pass

class Square(Shape):
	def __init__(self, side):
		self.side = side

	def area(self):
		return self.side * self.side

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return 3.14 * self.radius * self.radius

square = Square(5)
circle = Circle(3)

print(square.area())
print(circle.area())
