"""This version of ex24.py is commented to explain each step of the programme"""

print("Let's practice everything.")
# using the escape character \ before ' and \ tells Python
# to treat them as part of the string and not as escape sequences.
print('You\d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# strings delimited by triple quotes """ will not ignore whitespace
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)	# printing string stored in variable
print("--------------")

five = 10 - 2 + 3 - 6	# store result of math operation in five
print(f"This should be five: {five}.")	# formatted string syntax

def secret_formula(started):
	"""A function that returns the number of jelly_beans, jars, and crates
	given a 'started' number of ingredients"""
	jelly_beans = started * 500		
	jars = jelly_beans / 1000
	crates = jars / 100
	# return several values simultaneously as a list
	return jelly_beans, jars, crates


start_point = 10000
# similar to how we 'unpack' the argv list and store contents in different variables
# unpack list returned by calling secret_formula with start_point
# store results in beans, jars, crates in that order
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
# {} will store the variable(s) that are passed to .format as argument(s)
print("With a starting point of {}".format(start_point))

# it's just like with an f"" string
# same formatted string syntax as line 22
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# take current value of start_point, divide by 10, store result as new value of start_point
start_point = start_point / 10

print("We can also do that this way.")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# formula contains a LIST of vaulues that were returned by secret_formula
# the *formula argument passed to .format unpacks the list and replaces it with 
# ALL the variables it contains in order - these are the variables that are passed to the formatted string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))