class Logger:
	def log(self, message):
		return f"LOG: {message}"

class App:
	def __init__(self, logger):
		self.logger = logger

	def run(self):
		return self.logger.log("App started")

logger = Logger()
app = App(logger)

print(app.run())
