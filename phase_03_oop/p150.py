class Character:
	def __init__(self, name, hp):
		self.name = name
		self.hp = hp

	def is_alive(self):
		if self.hp > 0:
			return True

	def take_damage(self, amount):
		self.amount = amount
		self.hp -= amount

class Hero(Character):
	def attack(self):
		return 10

class Monster(Character):
	def attack(self):
		return 5

hero = Hero("Denis", 100)
monster = Monster("Goblin", 30)

print(hero.is_alive())
monster.take_damage(hero.attack())
print(monster.hp)
