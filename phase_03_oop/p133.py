class Swimmer:
	def swim(self):
		return "Swimming"

class Flyer:
	def fly(self):
		return "Flying"

class Duck(Swimmer, Flyer):
	def quack(self):
		return "Quack!"

duck = Duck()

print(duck.swim())
print(duck.fly())
print(duck.quack())
