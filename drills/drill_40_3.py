"""A version of the Song class with more features"""

class Song(object):
	"""Creates a Song object with song name, artist name, release year, and lyrics"""
	def __init__(self, name, lyrics, artist, year, genres):
		self.name = name
		self.lyrics = lyrics
		self.artist = artist
		self.year = year
		self.genres = genres

	def print_info(self):
		"""Prints formatted string showing info about song"""
		print(f"""Name of song: {self.name}Artist: {self.artist}\nReleased: {str(self.year)}\nArtist: {self.artist},\nGenres = {self.genres}""")

	def print_lyrics(self):
		"""Print each line in the lyrcis array, delimited by dotted lines"""
		print(f"Lyrics for {self.name.upper()}.");
		print("-" * 50)
		for line in self.lyrics:
			print(line)
		print("-" * 50)

# initialising array of lyrics to pass as argument
p_city_lyrics = ["Take me down to the Paradise City",
"Where the grass is green and the girls are pretty",
"Oh won't you please take me home",
"Yeah, yeah!"]

# intiialising instance of Paradise City
p_city = Song(name="Paradise City", lyrics=p_city_lyrics,
	year=1981, genres=["Pop", "Rock", "Classic Rock"], artist="Guns N' Roses")

# Testing print_info()
p_city.print_info()

# Testing print_lyrics()
p_city.print_lyrics()