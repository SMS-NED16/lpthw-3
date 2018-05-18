class Other(object):
	"""A simple class that Child delegates its tasks to"""
	def override(self):
		print("OTHER override()")

	def implicit(self):
		print("OTHER implicit()")

	def altered(self):
		print("OTHER altered()")


class Child(object):
	"""has-a Other object that it delegates its tasks to"""
	def __init__(self):
		# create an instance of the Other class that this instance can use
		self.other = Other()

	def implicit(self):
		# call the implicit() method from the other instance attribute
		self.other.implicit()

	def override(self):
		# Print a message - does not delegate this task to Other
		print("CHILD override()")

	def altered(self):
		# do something before calling the other attribute's altered function
		print("CHILD, BEFORE OTHER altered()")
		# call the other attributes altered function
		self.other.altered()
		# do something after calling the other attribute's altered funciton
		print("CHILD, AFTER OTHER altered()")

son = Child()	# create an instance of the Child class
son.implicit()	# call Other's implicit by calling Child's implicit
son.override()	# call Child's override 
son.altered()	# call Child's altered and call Other's altered in the process

print("""\n\nIt would have been better to make Other into a module instead of a class. The two 
classes have virtually identical code, with the only difference being that the Child class calls 
functions from the Other class. If Other was simply a module, we could have done the same thing 
without having to worry about class syntax when defining other, and wouldn't have to create an 
instance of Other() as an attribute of Child in order to call its functions.""")