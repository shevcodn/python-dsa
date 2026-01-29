class Team:
	def __init__(self):
		self.players = []

	def add(self, player):
		self.players.append(player)

	def __getitem__(self, index):
		return self.players[index]

team = Team()
team.add("Denis")
team.add("Ivan")
team.add("Max")

print(team[0])
print(team[2])
