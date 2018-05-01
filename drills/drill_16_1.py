"""A commented version of ex16.py"""

# importing the argv module from the sys package
# sys provides access to some objects used or maintained by the 
# interpreter for interacting with the interpreter
# argv - argument variable - the list of arguments passed to a Python script before runtime
from sys import argv

# unpacking the argv list to store the arguments passed to the Python script in variables for use in the programme
script, filename = argv

# Printing a message informing user that we will be removing contents of the data file
print(f"We're going to erase {filename}.")

# If the user enters CTRL-C, this is a keyboard interrupt. The programme stops.
print("If you don't want that, hit CTRL-C. (^C)")

# RETURN will allow the programme to continue i.e. the file will be removed
print("If you do want that, hit RETURN.")

# Input that will accept either keyboard interrupt or return
input("?")

# If the user entered open i.e. chooses to proceed with the operation
# The file is first opened to create a file object that is stored in target
print("Opening the file...")
target = open(filename, 'w')

# The target is then truncated or emptied using the truncate method defined for all file objects
print("Truncating the file. Goodbye!")
target.truncate()

# Ask the user for three lines that will be written to the recently truncated file
print("Now I'm going to ask you for three lines.")

# User input is stored in three separate strings
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these files to the file.")

# Using the write method to write each input to the new file. 
# To ensure each input occupies a separate line, we separate write ops by writing an end-of-line char
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Open -> Truncate -> Write operation complete. So close file
print("And finally, we close it.")
target.close()