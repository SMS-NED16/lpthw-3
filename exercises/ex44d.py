"""Shows all three forms of inheritance in one programme"""

class Parent(object):
	"""Create a Parent class that inherits from base class object"""
	def override(self):
		"""A function named override that prints to console"""
		print("PARENT override()")

	def implicit(self):
		"""A function named implicit that prints to console"""
		print("PARENT implicit()")

	def altered(self):
		"""A function named altered that prints to console"""
		print("PARENT altered()")

class Child(Parent):

	def override(self):
		"""An explicitly overridden version of the override function 
		from the parent class - prints 'CHILD override()' to console"""
		print("CHILD override()")

	def altered(self):
		"""Overrides behaviour before AND after the parent class version of alter runs"""
		print("CHILD, before PARENT altered()")
		super(Child, self).altered()
		print("CHILD, after PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()