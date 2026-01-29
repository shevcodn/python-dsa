class Animal:
	pass

class Dog(Animal):
	pass

class Cat(Animal):
	pass

def check_type(animal):
	if isinstance(animal, Dog):
		return "This is a dog"
	elif isinstance(animal, Cat):
		return "This is a cat"
	else:
		return "Unknown Animal"

dog = Dog()
cat = Cat()
animal = Animal()

print(check_type(dog))
print(check_type(cat))
print(check_type(animal))
