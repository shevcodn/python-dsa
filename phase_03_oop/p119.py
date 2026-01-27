class Car:
	def __init__(self, brand):
		self.brand = brand
		self.is_car_on = False
		self.mileage = 0

	def start(self):
		self.is_car_on = True

	def stop(self):
		self.is_car_on = False

	def drive(self, km):
		if self.is_car_on:
			self.mileage += km

	def get_info(self):
		return f"Brand: {self.brand}, Mileage: {self.mileage} km"


car = Car("Toyota")
car.drive(100)
car.start()
car.drive(50)
car.drive(30)
print(car.get_info())
car.stop()
