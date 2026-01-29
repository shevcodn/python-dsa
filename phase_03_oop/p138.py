class Playlist:
	def __init__(self):
		self.songs = []

	def add(self, song):
		self.songs.append(song)

	def __len__(self):
		return len(self.songs)

playlist = Playlist()
playlist.add("Song 1")
playlist.add("Song 2")
playlist.add("Song 3")

print(len(playlist))
