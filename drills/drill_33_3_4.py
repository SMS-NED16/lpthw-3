"""This version of ex33.py wraps the while loop in a function with arguments
to define the number of times the loop is run and the increment between
successive loops"""

def printWithWhile(number, step=1):
	"""This function prints all numbers fro 0 to numbers
	with an optional step argument defining the difference between successive nums"""
	i = 0
	numbers = [] 

	while (i < number):
		print(f"At the top, i is {i}.")
		numbers.append(i)

		i += step
		print("Numbers now:", numbers)
		print(f"At the bottom, i is {i}.")

	print("The numbers: ")

	for num in numbers:
		print(num)
	print("\n\n")



printWithWhile(6)
printWithWhile(6, 2)
printWithWhile(100, 10)