"""Exercise 44a - Action on child implies an action on the parent"""
class Parent(object):

	def implicit(self):
		print("PARENT implicit()")


class Child(Parent):
	pass	# create an empty block - create the class, but nothing to define


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

