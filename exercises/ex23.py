# importing sys module so we can use its built-in functions for interacting with the compiler
# specifically just one function/property - the argv - unpacks command line arguments
import sys 

# Python expects three argument variables when executing this script from the cmd line
# script - name of the file (ex23.py)
# input_encoding = character-encoding scheme for the value
# error = ?
script, input_encoding, error = sys.argv


# main part of the programme - this is where all the magic happens
def main(language_file, encoding, errors):
	# read the current line of the language_file object, store string in line
	line = language_file.readline()

	# if non-null value in line variable, then call print_line to echo line read
	if line:
		# what do the encoding and errors arguments do?
		print_line(line, encoding, errors)
		# is this a recursive call?
		return main(language_file, encoding, errors)


# function that actually prints the line from the file object to the console
def print_line(line, encoding, errors):
	# remove whitespace, store result in next_lang i.e. name of next language
	# more specifically, remove the trailing \n at the end of each line
	next_lang = line.strip()
	# convert string to bytes according to specified utf-8 encoding
	raw_bytes = next_lang.encode(encoding, errors=errors)
	# convert backs back to string according to specified utf-8 decoding
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	# show the encoded and decoded bytes relationship
	print(raw_bytes, "<===>", cooked_string)


# create a file object named languages by opening the ex23_languages.txt file
# also tell Python to store the file object with utf-8 encoding 
languages = open("ex23_languages.txt", encoding="utf-8")

# pass this file object to the main function to start decoding/encoding
main(languages, input_encoding, error)