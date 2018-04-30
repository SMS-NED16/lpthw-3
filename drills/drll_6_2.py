types_of_people = 10

x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

# 2/4 string-within-a-string insertions in line 9
# String 1 - binary, String 2 - do_not
y = f"Those who {binary} and those who {do_not}."

print(x)
print(y)

# 3/4 string-within-a-string insertions
print(f"I said: {x}")

# 4/4 string-within-a-string insertions
print(f"I also said: {y}")

hilarious = False

joke_evaluation = "Isn't that joke so funny? {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)