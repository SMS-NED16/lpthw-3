"""This file adds comments to each line so I can reinforce the concepts
being taught in the exercise"""

# Importing the argv module from the sys collection so we can access
# and unpack the argument variable passed to the Python call for this script
from sys import argv

# Unpacking the argv and storing its contents in script and user_name respectively
script, user_name = argv

# A symbol that will be printed to the console to prompt the user for input
# If we want to change the prompt symbol later on (from '> ' to '>>> '), then
# All we need to do is change the value of this variable and it will be updated in
# our entire programme
prompt = '> '

# Printing user's name and script name that were passed to the Python script
# as argument variables in the console
print(f"Hi {user_name}, I'm the {script} script.")

# Simple, non-formatted string so just use print
print("I'd like to ask you a few questions.")

# Ask the user for a response - runtime input - store in variable
print(f"Do you like me, {user_name}?")

# Display the '> ' symbol as a prompt, store result in likes
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# Print a multiline formatted string
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")