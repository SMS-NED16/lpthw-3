"""This script contains definition and different types of calls for
a function I have written"""

from sys import argv
script_name, arg_name, arg_age, arg_city, arg_hobbies = argv

def print_user_details(name, age, city, *hobbies):
	print(f"Information about {name.upper()}")
	print(f"Age:\t{age} years")
	print(f"So birth year = {str(2018 - int(age))}.")
	print(f"Current City:\t{city}")
	print(f"Hobbies Listed: {len(hobbies)}")
	for hobby in hobbies:
		print(f"\t* {hobby}")
	print("--------------------------------------")

def returnName():
	return "Saad Siddiqui"

def returnAge():
	return 21

def returnCity():
	return "Karachi"

def returnHobbies():
	return ['programming', 'pizza', 'procrastination', 'puppies']

# METHOD 1 - All arguments as values
print_user_details("Saad Mashkoor Siddiqui", 21, "Karachi", 
	"Programming", "Procrastination", "Pizza")

# METHOD 2 - All arguments as runtime variables
name = 'Saad'
age = 21 
city = 'Karachi'
hobbies = ['Programming', 'Procrastination', 'Reddit']
print_user_details(name, age, city, hobbies)

# METHOD 3 - Some variables, some literals
print_user_details(name, 21, hobbies)

# METHOD 4 - User input for some variables
ip_name = input("What is your name? ")
ip_age = input("What is your age?")
print_user_details(ip_name, ip_age, hobbies)

# METHOD 5 - Argv input for some variables
# print_user_details(arg_name, arg_age, arg_city, arg_hobbies)

# METHOD 6 - calling functions in argument list
print_user_details(returnName(), returnAge(), returnCity(), returnHobbies())