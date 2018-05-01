# Function definition for 'cheese and crackers' - takes two arguments
# cheese_count = number of cheese slices - implicitly assume int
# boxes_of_crackers = number of boxes of crackers - implicitly assume int
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# Access value passed as cheese_count and print to console
	print(f"You have {cheese_count} cheeses!")

	# Access value passed as boxes_of_crackers and print to console
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man, that's enough for a party!")
	print("Get a blanket.\n")


# Passing values 20 and 30 in place of cheese_count and boxes_of_crackers
print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

# Storing values in variables and passing these variables as arguments
print("OR, we can use variables from our script.")
amount_of_cheese = 10
amount_of_crackers = 50

# Access values stored in amount_of_cheese and amount_of_crackers
# And then substitute these values in place of cheese_count and boxes_of_crackers respectively
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too.")
# Evaluate expressions 10 + 20 and 5 + 6 to yield 30 and 11
# Set cheese_count to 30, boxes_of_crackers to 11 in function call
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math.")
# access value stored in amount_of_cheese, add 100, yield 110
# access value stored in amount_of_crackers, add 1000, yield 1050
# pass 110 and 1050 in place of cheese_count and boxes_of_crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 