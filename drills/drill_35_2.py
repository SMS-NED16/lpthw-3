# exit is a function defined in the sys module that allows us to
# gracefully exit the programme prematurely without an error code
from sys import exit

# this function defines the code that will be run in the gold room
def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn how to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greed bastard!")

# function run when player enters the bear_room
def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False
	# has to enter exact string for one of four predefined commands
	# otherwise the infinite loop will repeat itself
	while True:
		choice = input("> ")

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:	# evaluates to true if bear_moved = false
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True	# taunting once changes the bear_moved boolean flag
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("I got not idea what that means.")

# function is run when the player enters ctulhu's room
def ctulhu_room():
	print("Here you see the great evil Ctulhu.")
	print("He, it, whatever startes at you and go insane.")
	print("Do you flee for your life or eat your head?")

	choice = input("> ")

	# input can be a string containing the word 'flee' or 'head'
	# anything else will cause the ctulhu_room function call itself - recursion
	# recursive loop?
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well, taht was tasty!")
	else:
		ctulhu_room()

# dead is a funciton that prints why the player died whenever the player
# loses the game, and exits the programme gracefully with a call to exit(0)
def dead(why):
	print(why, "Good job!")
	exit(0)

# this is the function that starts the game
# can go left or right, if any other input - end game
def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	choice = input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		ctulhu_room()
	else:
		# call to dead with this argument exits the programme with the error message displayed 
		dead("You stumble around the room until you starve.")

start()