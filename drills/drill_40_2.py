"""This programme passes lyrics as variables instead of as inline literals"""

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

# initialising arrays of lyrics
p_city = ["Take me down to the paradise city",
"Where the grass is green and the girls are pretty",
"Oh won't you please take me home"]

will_he  = ["Cause I don't need to know", 
"I just want to make sure you're okay", 
"I don't need to know", 
"I just want to make sure you're all safe"]

shoot2thrill = ["Shoot to Thrill, Play to Kill",
"Too many women with too many pills",
"Shoot to thrill, Play to Kill",
"I got my gun at the ready gonna fire at will"]

# instantiating song objects and printing lyrics
paradise_city = Song(p_city)
willhe_joji = Song(will_he)
shoot_to_thrill = Song(shoot2thrill)

# echoing lyrics with call to sing_me_a_song
paradise_city.sing_me_a_song()
print("-" * 50)
willhe_joji.sing_me_a_song()
print("-" * 50)
shoot_to_thrill.sing_me_a_song()