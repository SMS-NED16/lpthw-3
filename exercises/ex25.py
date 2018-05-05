def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')	# Splits a sentence into words every time it encounters ' ' (space)
	return words  				# returns the list of words generated by the split function

def sort_words(words):
	"""Sorts the words."""	
	return sorted(words)		# sorted takes a list as an argument, creates a copy, sorts it, and returns

def print_first_word(words):
	"""Prints the first word after popping it off"""
	word = words.pop(0)			# removes and returns the element at index(0) i.e. first word in list of words
	print(word)					# print first word to console

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)		# negative index means start from the end of the list i.e. -1 = last element
	print(word)					# print last element

def sort_sentence(sentence):
	"""Takes a full sentence and returns the sorted words."""
	words = break_words(sentence)	# call a function within a function
	# break_words takes the sentence passed to sort_sentence as an argument, returns a list of all words
	# the list is then sorted by passing it to another function sort_words whose returned result is the final return list
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)	# first break the sentence into a list of words with call to break_words function
	print_first_word(words)			# then print the first word in the list of words you just generated
	print_last_word(words)			# print the last word in the list of words generated

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)	# sort sentence itself calls break_words and sort_words - encapsulation
	print_first_word(words)			# print first word
	print_last_word(words)			# print last word
