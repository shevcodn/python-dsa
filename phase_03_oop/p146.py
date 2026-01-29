class Engine:
	def __init__(self, horsepower):
		self.horsepower = horsepower

	def start(self):
		return "Engine started"


class Car:
	def __init__(self, brand, horsepower):
		self.brand = brand
		self.engine = Engine(horsepower)

	def start(self):
		return self.engine.start() + ", Car ready"

car = Car("BMW", 300)
print(car.engine.horsepower)
print(car.start())


