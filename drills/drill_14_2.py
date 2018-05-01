"""This drill changes the value stored in the prompt variable to something else 
entirely. The point of this exercise is to show the benefits of using a variable for
something like the input prompt as opposed to hardcoding values"""

from sys import argv

script, user_name = argv
prompt = '>>> '			# Changed from '> to >>>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")