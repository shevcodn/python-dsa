def double_result(func):
	def wrapper():
		result = func()
		return result * 2
	return wrapper

@double_result
def get_number():
	return 5

print(get_number())
