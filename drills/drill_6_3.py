types_of_people = 10

# Insert INTEGER, not a string
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# 2 STRING insertions - both binary and do_not are strings being placed in another string
y = f"Those who {binary} and those who {do_not}."

print(x)
print(y)

# 1 more STRING insertion - x itself is a string 
print(f"I said: {x}")

# 1 more STRING insertion - y is also a string
print(f"I also said: {y}")

hilarious = False

joke_evaluation = "Isn't that joke so funny? {}"
# BOOLEAN INSERTION, not string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# Not a string inside a string, but rather the joining of two strings 
print(w + e)