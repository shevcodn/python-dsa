import time

class Timer:
	def __init__(self):
		self.start_time = None


	def __enter__(self):
		self.start_time = time.time()

	def __exit__(self, *args):
		difference = time.time() - self.start_time
		print(f"Elapsed: {difference:.2f} seconds")

with Timer():
	time.sleep(2)
	print("Working...")
