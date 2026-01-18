class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height
	def perimeter(self):
		return 2 * self.width + 2 * self.height


r = Rectangle(5, 3)
print(r.area())
print(r.perimeter())

r2 = Rectangle(10, 10)
print(r2.area())
print(r2.perimeter())

