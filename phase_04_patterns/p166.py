class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def greet(self):
		return f"hi, I'm {self.name}"

class Employee(Person):
	def __init__(self, name, age, salary):
		super().__init__(name, age)
		self.salary = salary

	def get_bonus(self):
		return self.salary * 0.1

	def greet(self):
		return f"Hi, I'm {self.name}, I work here"

p = Person("Alex", 25)
print(p.greet())

e = Employee("Denis", 21, 5000)
print(e.greet())
print(e.get_bonus())
