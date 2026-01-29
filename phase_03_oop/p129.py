class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def work(self):
		return "Working..."

class Manager(Employee):
	def work(self):
		return "Managing team"

class Developer(Employee):
	def work(self):
		return "Writing code"

manager = Manager("Alice", 80000)
dev = Developer("Bob", 60000)

print(manager.name)
print(manager.salary)
print(manager.work())
print(dev.work())
