class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name}, {self.age} years"

class Employee(Person):
	def __init__(self, name, age, salary):
		super().__init__(name, age)
		self.salary = salary

	def __str__(self):
		return f"{self.name}, {self.age} years, ${self.salary}"

p = Person("Alex", 25)
print(p)

e = Employee("Denis", 21, 5000)
print(e)
print(e.name)
print(e.salary)
