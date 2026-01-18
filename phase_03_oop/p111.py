class Timer:
	def __init__(self, seconds):
		self.seconds = seconds

	def get_minutes(self):
		return self.seconds // 60


	def get_remaining(self):
		return self.seconds % 60


t = Timer(125)
print(t.get_minutes())
print(t.get_remaining())

t2 = Timer(60)
print(t2.get_minutes())
print(t2.get_remaining())

t3 = Timer(45)
print(t3.get_minutes())
print(t3.get_remaining())
