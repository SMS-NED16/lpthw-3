"""This version of ex32.py tests if a range function call can be used
to initialise a list of numbers i.e. if it is possible to use range outside
of a for loop"""

the_count = range(1, 6)	# replacing [1, 2, 3, 4, 5]
fruits = ['apples', 'bananas', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print(f"This is count: {number}.")

# same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}.")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
	print(f"I got {i}.")

# directly initialising elements with call to range
elements = range(0, 6)

# does it work?
for element in elements:
	print(f"{element} was added to the 'elements' list.")

print("""
The results of the first and last for loops show that it is indeed
possible to initialise a list directly using the range function. 
This means  the range -> for -> append method of initialising a list 
is needlessly complicated.""")