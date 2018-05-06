from sys import argv        # importing the argv module because the code requires cmd line argument unpacking

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()          # added a missing height variable - this will take the input for 'How tall are you?'
print("How much do you weigh?", end=' ')    # added a missing closing parenthesis )
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename)    # fixed filenme to filename

print("Here's your file {filename}:")
print(txt.read())       # fixed variable name from tx to txt

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) # changed text_again_read() to text_again.read() - this is because .read is a function defined for file objects


print('Let\'s practice everything.')    # The apostrophe in lets no longer acts as a string delimiter
print('You\'d need to know \'bout escapes ' +       # string concatenation helps split print argument over two lines
    'with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") # added a missing string delimiter " at end of print argument
print(poem)
print("--------------") # added a missing string delimiter " at beginning of print argument


five = 10 - 2 + 3 - 6   # completed expression so that it evaluates to 5
print(f"This should be five: {five}")   # added a missing parenthesis for print argument

def secret_formula(started):    # added a colon at the end of the def - prevents indentation errors
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # added third argument crates - secret_formula returns three values

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) # changed startpoint to start_point 
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30       # changed spelling of cates variable to cats
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")    # added argument parentheses for print statements

if people > cats:       # fixed logic error - people should be more than cats for world to be saved
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:       # added a missing colon for the if statement
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:  # added a missing colon for the if statement
    print("People are less than or equal to dogs.") # added a missing " delimiter for the print argument


if people == dogs: # changed = to == for a comparison operation instead of assignment
    print("People are dogs.")
