class Temperature:
	def __init__(self, celsius):
		self.celsius = celsius

	def to_fahrenheit(self):
		return self.celsius * 9 / 5 + 32

t = Temperature(0)
print(t.to_fahrenheit())

t2 = Temperature(100)
print(t2.to_fahrenheit())

t3 = Temperature(25)
print(t3.to_fahrenheit())
