"""This version of ex31.py adds additional decisions to the game"""

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
	print("There is a giant bear here eating a cheesecake.")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")
	print("3. Run away from the bear.")

	bear = input("> ")

	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	elif bear == "3":
		print("Smart move!")
		print("You ran away.")
	else:
		print(f"Yes, doing {bear} is probably better.")

elif door == "2":
	print("You stare into the endless abyss at Ctulhu's retina.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")
	print("4. Wave.")

	insanity = input("> ")
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a mind of jello.")
		print("Good job!")
	elif insanity == "4":
		print("Ctulhu blinks back. Good job! You are now best friends with Ctulhu.")
	elif insanity == "3":
		print("You should not have listened to the melodies. We will miss you.")
	else:
		print(f"Yes, doing {insanity} when looking Ctulhu in the eye is probably the best idea.")

elif door == "3":
	print("Congratulations! You found the secret door!")
	print("You see Thanos sitting on a hill looking at the sun rise over a grateful world.")
	print("What do you do?")
	print("1. Punch Thanos in the face. He deserves it.")
	print("2. Punch Thanos in the face. He deserves it.")
	print("3. Say 'Hello there' like Obi-Wan Kenobi.")
	print("4. Not feel so good.")
	thanos = input("> ")

	if input == "1":
		print("It wasn't very effective. Thanos returns your punch with his a smug grin.")
	elif input == "2":
		print("It wasn't very effective. Thanos drops you harder than he dropped Gamora.")
	elif input == "3":
		print("It was super effective! Thanos responds by saying 'General Kenobi'.")
	elif input == "4":
		print("Too soon, man. Too soon.")
	else:
		print("Snap! You don't exist any more.")

else:
	print("You stumble around and fall on a knife and die. Good job!")