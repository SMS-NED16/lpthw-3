"""This version of ex30.py is commented to explain each line of code"""
# initialising variables
people = 30
cars = 40
trucks = 15		

# Access values in 'cars' and 'people' - check if cars > people
# If true, execute the indented print statement. Otherwise, skip to next block
if cars > people:
	print("We should take the cars.")	

# This block only executes if the previous block was skipped i.e. if cars > people evaluates to False
# Try evaluating cars < people; If true, print indented statement i.e. run this block
elif cars < people:
	print("We should not take the cars.")	# actually skipped for these values
# If both if and elif blocks don't evaluate to true, run this block
else:
	print("We can't decide.")

# Evaluate trucks > cars - if true, run indented statement. Otherwise, move on to the next line.
if trucks > cars:
	print("That's too many trucks.")

# If the previous if conditional does not evaluate to True, try evaluating
# the following block. If true, run indented code. Otherwise, skip.
elif trucks < cars:
	print("Maybe we should take the trucks.")
# If the if and the elif blocks both skipped, then run this block
else:
	print("We still can't decide.")

# This if-else statement has only two alternatives - the if branch or the else branch
if people > trucks:
	print("Alirght, let's just take the trucks.")
# no elif branch
else:
	print("Fine, let's just stay home then.")