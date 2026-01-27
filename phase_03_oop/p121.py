class Quiz:
	def __init__(self):
		self.questions = {}
		self.score = 0

	def add_question(self, question, answer):
		self.questions[question] = answer

	def ask(self, question, user_answer):
		if user_answer == self.questions[question]:
			self.score += 1

	def get_score(self):
		return self.score

q = Quiz()
q.add_question("2+2", "4")
q.add_question("Столица Канады?", "Ottawa")

q.ask("2+2", "4")
q.ask("Столица Канады?", "Ottawa")
print(q.get_score())
