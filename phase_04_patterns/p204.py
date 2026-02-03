def add_exclamation(func):
	def wrapper(name):
		result = func(name)
		return result + "!"
	return wrapper

@add_exclamation
def greet(name):
	return f"Hello {name}"

print(greet("Denis"))
