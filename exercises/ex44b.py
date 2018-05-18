"""Exercise 44b - Override Explicitly"""

class Parent(object):

	def override(self):
		print("PARENT override()")

class Child(Parent):
	# same function name and arguments as Parent class
	def override(self):
		print("CHILD override()")	# but different implementation


dad = Parent()
son = Child()

dad.override()
son.override()