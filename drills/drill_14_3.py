"""This script is written such that it expects an additional argument value when
executed. The point of this exercise is to show that we can take an arbitrary number
of argument values and an arbitrary number of runtime input values."""

from sys import argv

script_name, name, age = argv
prompt = "> "


print(f"Hi {name}, this is the {script_name} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {name}?")
likes = input(prompt)

print(f"Where do you live, {name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so your name is {name} and you're {age} years old.
You said {likes} about liking me. 
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
