"""This version of ex33.py wraps the while loop in a function
that can be called with different arguments to modify the number
of times the loops is run"""

def printNumbers(num):
	i = 0
	numbers = []

	while i < num:
		print(f"At the top, i is {i}.")
		numbers.append(i)

		i += 1
		print("Numbers is now", numbers)
		print(f"At the bottom, i is {i}.")
	
	for num in numbers:
		print(num, end=" ")
	print("\n\n")

printNumbers(6)
printNumbers(3)
