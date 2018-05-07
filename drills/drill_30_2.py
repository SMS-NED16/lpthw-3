people = 50
cars = 55
trucks = 80

if cars > people:	# 55 > 50, so if statement executed
	print("We should take the cars.")
elif cars < people:	# this block is skipped because if is executed
	print("We should not take the cars.")
else:				# this block is skipped because if is executed
	print("We can't decide.")

if trucks > cars:	# 80 > 55	# if block executed
	print("That's too many trucks.")
elif trucks < cars:				# skipped
	print("Maybe we could take the trucks.")
else:							# skipped
	print("We still can't decide.")


if people > trucks:	# false - if block skipped
	print("Alright, let's just take the trucks.")
else:				# true - this block will run
	print("Fine, let's just stay home then.")