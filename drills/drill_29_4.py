"""This version of ex29.py uses different boolean expressions
in the conditions for the if statements"""

people = 30
cars = 40
trucks = 15

if cars != people:
	print("Cars are not equal to people.")

if cars >= trucks:
	print("Cars are greater than or equal to trucks.")

if cars <= people:
	print("Cars are less than or equal to people.")

if (cars >= people and cars <= trucks):
	print("Cars are neither more than people nor less than trucks.")

if (people == trucks or (trucks != people and cars >= trucks)):
	print("This is a complicated Boolean expression that I won't even try to solve.")

