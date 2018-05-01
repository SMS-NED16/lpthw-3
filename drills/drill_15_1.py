# importing the argv module from the sys collection so that we can pass
# argument variables to our Python script when we call it from the terminal
from sys import argv

# Unpacking the argument variable and storing its contents in the variables
# script and filename - script is the name of the Python script being executed
# filename is the name of the txt file from which data will be read
script, filename = argv

# Using Python's built-in open function to read data stored in the file with the name
# or filepath 'filename' that is passed to it as an argument. 
# this function returns a filestream object
txt = open(filename)

# Using a formatted string that uses one of the argument variables 
print(f"Here's your file {filename}.")

# Calling txt.read which a function defined for filestream objects that allows data
# stored in these objects to be returned as a string
# Printing the string returned by read in one line
print(txt.read())

# Print a message asking the user to enter the name of the text file/path to the file again
print("Type the filename again.")

# Storing the result of the input operation in file_again - user defined filepath
file_again = input("> ")

# Once again, calling the open function on the file(path) that returns a filestream object
# containing information about the file the user entered
txt_again = open(file_again)

# Calling the read method on this file and printing the returned string
print(txt_again.read())