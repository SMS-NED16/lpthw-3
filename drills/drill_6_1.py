# Create a variable named types_of_people and store the value 10 in it
types_of_people = 10

# Create a formatted string 'There are 10 types of people'
# using the value stored in the types_of_people variable, assign result to x
x = f"There are {types_of_people} types of people."

# Store values for variables binary and do_not
binary = "binary"
do_not = "don't"

# Create a formatted string using the values stored in the binary and do_not variables
# "Those who binary and those who don't".
# Store this string in the variable y
y = f"Those who {binary} and those who {do_not}."

# Print both formatted strings
print(x)
print(y)

# Nesting of formatted strings
# Create a new formatted string using formatted string x and print result directly
print(f"I said: {x}")
# Create a new formatted stirng using formatted string y and print result directly
print(f"I also said: {y}")

# Create a boolean variable `hilarious` and set it to false
hilarious = False

# Create formatted string using a null object or 'blank' that will later be filled by a variable
# The string reads "Isn't that joke so funny? [VARIABLE HERE]"
joke_evaluation = "Isn't that joke so funny? {}"

# Use the .format method on the joke_evaluation string and pass it an argument hilarios
# This will insert the value of the `hilarious` variable inside the {} of the 
# joke_evaluation string
print(joke_evaluation.format(hilarious))

# Create two strings
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate them and print the result
print(w + e)