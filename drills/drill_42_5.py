"""This programme creates a class that has lists and dictionaries as attributes
to demonstate the use of is-a and has-a relationships between objects"""

class Animal(object):
	"""A basic Animal abstract class"""
	pass

class Dog(Animal):
	"""A specialised version of the Animal class to represent dogs"""
	def __init__(self, name):
		"""Constructor to initialise names"""
		self.name = name

class Cat(Animal):
	"""A specialised version of the Animal class to represent dogs"""
	def __init__(self, name):
		"""Contructor in initalise names"""
		self.name = name

class Person(object):
	"""A simple class to represent a Person, their pets, and their favourite dog/cat"""
	def __init__(self, name):
		"""Initialise name with argument; Also init dogs, cats as lists and dict
		of favourite animals"""
		self.name = name
		self.dogs = [Dog("Rusty"), Dog("Fuzzy"), Dog("Bear")]
		self.cats = [Cat("Bambi"), Cat("Chubby"), Cat("Fluff")]
		self.favourites = {'Cat': Cat("Whiskers"), 'Dog': Dog("Borko")}

	def print_info(self):
		"""Print information about the Person object"""
		print(f"Name:\t{self.name}.")
		print("List of dogs.")
		# has-a list of dogs - print name of each Dog object
		for dog in self.dogs:
			print(f"\t- {dog.name}")
		# has-a list of cats - print name of each Cat object
		print("List of cats.")
		for cat in self.cats:
			print(f"\t- {cat.name}.")
		# Print key-value pairs of favourite animals dict
		print("Favourite Pets:")
		for animal, pet in self.favourites.items():
			print(f"\t{animal}:\t{pet.name}")


# Testing the class by instantiating a Person
saad = Person("Saad Mashkoor Siddiqui")
saad.print_info()
