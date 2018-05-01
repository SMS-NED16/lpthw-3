# importing the argv module from the sys package so we can 
# access the argument variables passed to our Python script in the command line
from sys import argv

# Unpacking the argument variables list and storing contents in 
# variables that can be used in the Python script
script, input_file = argv

# A function that takes a file object f as an argument, reads its contents
# and prints the entire contents of the file to the console
def print_all(f):
	print(f.read())

# A function that takes a file object f as an argument and 
# 'goes to' the 0th or first line in the file. This is useful
# if we're accessing data in a file object and want to return to the
# beginning for some reason
def rewind(f):
	f.seek(0)

# Takes two arguments - `line count` and a file object f
# This function prints out a single line of the file object instead of all the lines
# The current line being printed is kept track of using the line_count variable
# Beause the line_count variable is incremented after each call to this function i.e.
# each call to the read_line function (after which the file 'seeks' to the next line)
def print_a_line(line_count, f):
	print(line_count, f.readline())

# Open the target file in read mode and return a file object
current_file = open(input_file)

print("First, let's print the whole file:\n")

# Pass the target file's object as argument to the print_all method to print all contents
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Pass target file obj to rewind function that will use the seek(0) method
# to position the file object's parser at the beginning of the file - it was previously 
# at the end of the file after the previous print_all call
rewind(current_file)

print("Let's print three lines:")

# Currently on the first line so print it 
current_line = 1
print_a_line(current_line, current_file)	# print first line

# Increment the current_line - the readline() method will have done
# this implicitly in the file obj
current_line = current_line + 1
print_a_line(current_line, current_file)	# print second line

current_line = current_line + 1
print_a_line(current_line, current_file)	# print third line