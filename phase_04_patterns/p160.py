class Playlist:
	def __init__(self, name):
		self.name = name
		self.songs = []

	def add_song(self, song):
		self.songs.append(song)


	def __len__(self):
		return len(self.songs)

p = Playlist("Rock")
print(len(p))

p.add_song("Song 1")
p.add_song("Song 2")
print(len(p))
