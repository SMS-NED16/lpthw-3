"""Some more practice with lists and their elements"""

courses = ['Signals', 'Statistics', 'Fields', 'Digital', 'Instruments']

for index in range(0, len(courses)):
	print("The " + str(index + 1) + "th course is " + courses[index] + ".")
	print("This course is at index number: " + str(index))

print("\n\n\n")
students = ['Saad Mashkoor Siddiqui',
			'Faiq Siddiqui',
			'Syed Abdul Haseeb Qadri',
			'Malik Zain-ul-Hassan',
			'Waleed Hasan',
			'Syed Najam Mehdi',
			'Mirza Moiz Haider']
for index in range(0, len(students)):
	print("The " + str(index + 1) + "th student is " + students[index] + ".")
	print("This student is at index " + str(index) + " in the list.")

