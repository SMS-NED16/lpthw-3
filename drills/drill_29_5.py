"""This version of ex29.5 py changes the values of people, cats, and dogs"""
people = 1000
cats = 40
dogs = 50000

if people < cats:
	print("Too many cats! The world is doomed!")

if people > cats:
	print("Not many cats! The world is saved!")

if people < dogs:
	print("The world is drooled on!")

if people > dogs:
	print("The world is dry!")

dogs += 75

if people >= dogs:
	print("People are greater than or equal to dogs.")

if people <= dogs:
	print("People are less than or equal to dogs.")


if people == dogs:
	print("People are dogs.")

print("""
Because the values of people, cats, and dogs have been changed
therefore the conditional statements no longer evaluate to the 
same Boolean values as the ones in ex29.py. This means that a 
different combination of if statements is executed while others 
are not.""")