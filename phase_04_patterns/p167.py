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


class Manager(Employee):
	def __init__(self, name, age, salary, team_size):
		super().__init__(name, age, salary)
		self.team_size = team_size

	def get_bonus(self):
		return self.salary * 0.2 + self.team_size * 100

e = Employee("Alex", 30, 5000)
print(e.get_bonus())

m = Manager("Denis", 25, 6000, 5)
print(m.get_bonus())
print(m.salary)
