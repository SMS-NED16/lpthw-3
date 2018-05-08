"""This is my own version of a text-based game 
choose-your-own-adventure game implemented with nested conditionals"""

print("You wake up in bed with a serious case of the Mondays.\nWhat do you do?")
print("What do you do?")
print("1. Go back to bed.")
print("2. Get out of bed and go to uni.")
print("3. Stay at home and decide to code.")
stage_1 = input("> ")

if stage_1 == "1":
	print("Good job! You're an adult. You don't have to worry about responsibilities!")
elif stage_1 == "2" or stage_1 == "3":
	print("Good! at least you're being productive!")
	if stage_1 == "2":
		print("You decide to go to university. Best not to miss classes")
		print("The monotony of university makes you want to cry. What do you do?")
		print("1. Bear with it and continue like a normal person.")
		print("2. Run back home and go to sleep.")
		uni = input("> ")
		if uni == "1":
			print("Good job! Solider on!")
		else:
			print("Good job! You're an adult. You don't have to worry about making responsibilities!")	
	else:
		print("Okay, so you decide to stay home and code. What do you have in mind?")
		print("1. Learn Python the Hard Way")
		print("2. Web Development - Rob Percival")
		print("3. Web Development - Colt Steele.")
		print("4. Java - Deitel.")
		print("5. C++ - Deitel.")
		prog = input("> ")
		if prog == "1":
			print("Python is fun!")
		elif prog == "2" or prog == "3":
			print("Good job! You need to get this done ASAP.")
		elif prog == "4" or prog == "5":
			print(f"Yeah, good choice! You've been meaning to this for a while.")
		else:
			print("Well, as long as you're doing something!")
else:
	print(f"{stage_1}? You can't just do that! What do you think this is? Real life?")		