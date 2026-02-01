class Temperature:
	def __init__(self, celsius):
		self._celsius = celsius

	@property
	def celsius(self):
		return self._celsius

	@celsius.setter
	def celsius(self, value):
		if value < -273.15:
			raise ValueError("Temperature below absolute zero!")
		self._celsius = value

t = Temperature(25)
print(t.celsius)

t.celsius = 100
print(t.celsius)

t.celsius = -300
