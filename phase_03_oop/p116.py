class LightSwitch:
	def __init__(self):
		self.is_on = False

	def toggle(self):
		self.is_on = not self.is_on

	def is_lit(self):
		return self.is_on


light = LightSwitch()
print(light.is_lit())

light.toggle()
print(light.is_lit())

light.toggle()
print(light.is_lit())

light.toggle()
light.toggle()
light.toggle()
print(light.is_lit())
