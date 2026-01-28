class Vehicle:
	def __init__(self, brand):
		self.brand = brand

	def move(self):
		return ("Moving...")

class Car(Vehicle):
	def move(self):
		return ("Driving on 4 wheels")

class Bike(Vehicle):
	def move(self):
		return ("Riding on 2 wheels")

car = Car("Toyota")
bike = Bike("Yamaha")

print(car.brand)
print(car.move())
print(bike.move())
