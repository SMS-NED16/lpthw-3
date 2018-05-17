"""This programme attempts to use a class as an object"""

class MyClass(object):
	def __init__(self, name):
		if (name):
			self.name = name
		else:
			self.name = "Sugoi Senpai"


	def printName():
		print(f"Calling a class function")

	age = 18;			# static variable




print(MyClass)			# printing entire Class, just like an object
print(type(MyClass))	# printing type of class
print(MyClass.age)		# accessing age variable of Class - treating it as an object
MyClass.printName()		# calling a function with dot operator - same as object

print("""
This programme shows that it is indeed possible to use a class
as an object. This programme defines a class named MyClass and within
it creates a variable age and a function printName that is not tied to any
specific instance of MyClass (it does not take a `self` argument.)

The fact that we can access the age variable and call the printName function
with the dot operator shows that a class can indeed behave like an object.
""")