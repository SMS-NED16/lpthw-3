"""This script contains some of my own functions that return different values"""

def square(num):
	"""Returns the square of the number passed as an argument"""
	return num * num

def cube(num):
	"""Returns the cube of the number passed as an argument"""
	return num ** 3

def getInitials(name):
	"""Takes a name, splits it into different words, returns the first letter of each word"""
	nameList = name.split(' ')
	initials = ""
	for name in nameList:
		initials += name[0].upper() + ". "
	return initials

print(square(1001))
print(cube(1001))
print(getInitials("Saad Mashkoor Siddiqui"))