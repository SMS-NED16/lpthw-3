import random	# for randomly selecting a key-value pair from the dictionary
# importing the urlopen function from the request class of the urllib module
# this allows us to make an HTTP request to a URL (a web address) to access the list of words/phrases
from urllib.request import urlopen

# for argv - unpacking argument variables when calling the script from the command line
# useful because we may want to pass the 'english' option to the script 
# i.e. an inverse version of the script in which we enter OOP expressions for a given english statement
import sys

# URL of word list
WORD_URL = "https://learncodethehardway.org/words.txt"

# empty list that will be used to store words fetched from the URL
WORDS = []

# Phrases dictionary maps OOP fill-in-the-blank type phrases with english fill-in-the-blank type phrases
# this is a dictionary of questions and answers that will be used as templates for different words
PHRASES = {
	# %%% is a placeholder for class names 
	# *** is a placeholder for parameters
	"class %%%(%%%):":"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef__init__(self, ***)": "class %%% has-a __init__ that takes self and *** params.",
	# here, *** is a placeholder for the function name while @@@ is a placeholder for parameters
	"class %%%(object):\n\tdef ***(self, @@@)":"class %%% has-a function *** that takes self and @@@ params.",
	# *** is a placeholder for a variable name %%% is a placheholder for a class name
	"*** = %%%()": "Set *** to an instance of class %%%.",
	# *** = placeholder for variable name/attribute; @@@ = parameter
	"***.***(@@@)": "From *** get the *** function, call it with params self, @@@.",
	# *** is a placeholder for a variable name/attribute/literal or value
	"***.*** = '***'": "From *** get the *** attribute and seti to '***'."
	}

# do they want to drill phrases first
# if the Python script has been called with the additional 'english' option
# that means the user wants to write OOP code corresponding to specific phrases
# set flag variable accordingly
if len(sys.argv) == 2 and sys.argv[1] == 'english':
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# load up the words from the website
# open the url, form a file object of its contents, read all the lines
# add each line to the WORDS list after removing whitespace, utf-8 format, and typecasting to string
for word in urlopen(WORD_URL).readlines():
	WORDS.append(str(word.strip(), encoding="utf-8"))


# convert a key-value pair from PHRASES into a Q-A pair using word list
def convert(snippet, phrase):
	# make a list of all class names
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	
	# make a list of all variable names
	other_names = random.sample(WORDS, snippet.count("***"))
	
	# empty list to store result of Q-A insertion operation
	results = []

	# empty list to store parameter names from WORD
	param_names = []

	# count the number of @@@ occurrences in snippet i.e. number of times parameter placeholder appears
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(
			random.sample(WORDS, param_count)))

	# something about list slicing
	for sentence in snippet, phrase:
		result = sentence[:]

		# fake class names
		for word in class_names:
			# replace the first occurrence of the %%% placeholder in the 
			# string with the current word in class_name 
			# store the modified string in result
			result = result.replace("%%%", word, 1)

		# fake other names
		# do the same thing for variable names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		# do the same thing for parameter names - parameter names have been
		# generated in required qty by param^ generator block above
		for word in param_names:
			result = result.replace("@@@", word, 1)

		# append the final string to the list of results
		results.append(result)

	# return the phrase-snippet pair
	return results


# keep going until they hit CTRL-D
try:
	while True:
		# snippets - stores OOP code examples as a list
		snippets = list(PHRASES.keys())

		# randomise the order of the snippets list 
		random.shuffle(snippets)

		# for every OOP code line in the snippets list
		for snippet in snippets:
			# the answer phrase is accessed from the phrases dictionary
			phrase = PHRASES[snippet]
			# the answer phrase and code sample are passed to the convert function to 
			# get back a Q-A pair
			question, answer = convert(snippet, phrase)
			# if the user has decided to write code instead of description, thenchange order of Q/A
			if PHRASE_FIRST:
				question, answer = answer, question;

			# print the question - either code snippet or phrase
			print(question)
			# prompt the user for input 
			input("> ")
			# Output the answer, regardless of right or wrong
			print(f"ANSWER: {answer}\n\n")
except EOFError:
	print("\nBye")
