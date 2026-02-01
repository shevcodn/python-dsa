class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	@property
	def area(self):
		return self.width * self.height

	@property
	def perimeter(self):
		return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print(rect.area)
print(rect.perimeter)
