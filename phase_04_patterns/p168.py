class Vehicle:
	def __init__(self, brand, year):
		self.brand = brand
		self.year = year

	def start(self):
		return f"{self.brand} started"

class Car(Vehicle):
	def __init__(self, brand, year, fuel_type):
		super().__init__(brand, year)
		self.fuel_type = fuel_type

	def refuel(self):
		return f"Refueling with {self.fuel_type}"

v = Vehicle("Toyota", 2020)
print(v.start())

c = Car("BMW", 2022, "petrol")
print(c.start())
print(c.refuel())
print(c.year)
