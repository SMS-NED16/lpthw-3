# Print a string - straightforward
print("Mary had a little lamb.")

# First, create a string with the value 'Its fleece was white as [blank]'
# Then, use the format method on this string to 'fill in the blank'
# By passing 'snow' as an argument to the format method
# The result of this chain of operations will be a string
# "Its fleece was white as snow." - print it
print("Its fleece was white as {}.".format('snow'))

# Yet another straightforward string printing operation
print("And everywhere that Mary went.")

# Print out the string "." 10 times - when the * operator is used
# in this way ('s' * num), it means print the string 's' num number of times
print("." * 10)		# What did that do?

# Initialise variables to store each of the letters of the word 'Cheeseburger'
end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# Watch that comma at the end. Try removing it to see what happens
# Concatenate the first six letters (end1 - end6) to make a string 'Cheese'
# Then, the end=' ' argument to the print method adds a space to the end of the print result 
# Removing the last ' delimiter for the end argument leads to an EOF syntax error
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')

# Same concatenation as last time, but no end argument. This is because 
# Cheese Burger doesn't need a space after the Burger
print(end7 + end8 + end9 + end10 + end11 + end12)