# Create a string named formatter that has spaces for four different variables
formatter = "{} {} {} {}"

# Call the format method on the formatter string, which takes an argument for each
# of the 'spaces'/'blanks' in the formatter string and inserts the arguments in them
# The formatter string therefore acts as a template for printing out a list of values 
# separated by a space - these values can be passed as literal or variable arguments
print(formatter.format(1, 2, 3, 4))	# 1 2 3 4
print(formatter.format("one", "two", "three", "four"))	# one two three four
print(formatter.format(True, False, False, True))	# True False False True
# Prints 16 {} - nests 4 formatter strings, each as 4 {}
print(formatter.format(formatter, formatter, formatter, formatter)) 

# The arguments can also be passed on separate lines like this, whitespace is ignored
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))