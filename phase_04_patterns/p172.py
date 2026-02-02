class Player:
	def __init__(self, name, position):
		self.name = name
		self.position = position

	def __str__(self):
		return f"{self.name} ({self.position})"

class Team:
	def __init__(self, team_name):
		self.team_name = team_name
		self.players = []

	def add_player(self, player):
		self.players.append(player)

	def show_roster(self):
		for player in self.players:
			print(player)

team = Team("Warriors")

team.add_player(Player("Curry", "Guard"))
team.add_player(Player("Durant", "Forward"))

team.show_roster()
