class Timer:
	def __enter__(self):
		print("Timer started")
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		print("Timer stopped")

with Timer():
	print("Doing work...")
