class TodoList:
	def __init__(self):
		self.list = []

	def add(self, task):
		self.list.append(task)

	def complete(self, task):
		self.list.remove(task)

	def show(self):
		return self.list

todo = TodoList()
todo.add("Buy Milk")
todo.add("Learn Python")
todo.add("Gym")
print(todo.show())
todo.complete("Gym")
print(todo.show())
