"""This version of ex33.py is written with a for loop instead of the while loop"""
i = 0
numbers = []

for i in range(0, 6):
	print(f"i is : {i} at top of for loop.")
	numbers.append(i)
	i += 1
	print("Numbers is now", numbers)
	print(f"i is: {i} at the bottom of for loop.")

print("The numbers: ")
for number in numbers:
	print(number)

print("""
There is no need for the increment operation in the loop
because the for loop handles that automatically. At the end 
of each iteration of the for loop, the value of i is automatically
incremented. 

Leaving the increment operation in the loop does not seem to affect
the value of the i variable in the for loop. Not sure why.
""")
