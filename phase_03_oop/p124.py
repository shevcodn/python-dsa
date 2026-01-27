class Stopwatch:
	def __init__(self):
		self.time = 0
		self.is_watch_on = False

	def start(self):
		self.is_watch_on = True

	def stop(self):
		self.is_watch_on = False

	def tick(self):
		if self.is_watch_on == True:
			self.time += 1

	def get_time(self):
		return self.time

sw = Stopwatch()
sw.tick()
sw.start()
sw.tick()
sw.tick()
sw.tick()
print(sw.get_time())
sw.stop()
sw.tick()
print(sw.get_time())
