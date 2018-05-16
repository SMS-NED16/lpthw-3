class Song(object):
	"""This class creates simple songs using an array of lyrics"""

	def __init__(self, lyrics):
		"""Initialises Song object using array of lyrics"""
		self.lyrics = lyrics

	def sing_me_a_song(self):
		"""Prints every lyric line"""
		for line in self.lyrics:
			print(line)

# initialising Paradise City Song object
paradise_city = Song(["Take me down to the Paradise City",
	"Where the grass is green and the girls are pretty",
	"Oh, won't you please take me home? Yeah, yeah!"])

# initialise Will_He
will_he = Song(["'Cause I don't need to know",
	"I just want to make sure you're okay",
	"I don't need to know",
	"I just want to make sure you're all safe"])

# initialising Shoot to Thrill
shoot_to_thrill = Song(["Shoot to Thrill, Play to Kill",
	"Too many women with too many pills",
	"Shoot to Thirll, Play to Kill",
	"I got my gun at the ready, gonna fire at will."])

# echoing lyrics by calling sing_me_a_song for each object
paradise_city.sing_me_a_song()
print("-" * 50)
will_he.sing_me_a_song()
print("-" * 50)
shoot_to_thrill.sing_me_a_song()
print("-" * 50)