"""This version of exercise 42 adds functions to the base classes
people, fish, and animal to make them do things."""

class Animal(object):
	def __init__(self, name, sound):
		self.name = name
		self.sound = sound

	def make_sound(self):
		print(f"{self.name.title()} says {self.sound.upper()}.")

	def move_around(self):
		print(f"{self.name.title()} moved around.")


class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name, sound="Bork")
		self.breed = "Pomsky"

class Cat(Animal):
	def __init__(self, name):
		super(Cat, self).__init__(name, sound="Meow")
		self.breed = "Tabby"

class Fish(object):
	def __init__(self, name, species, fins, isCarnivore):
		self.name = name
		self.species = species
		self.fins = fins
		self.isCarnivore = isCarnivore

	def print_info(self):
		print(f"Name:\t{self.name}.")
		print(f"Species:\t{self.species}.")
		print(f"Fins:\t{self.fins}.")
		print(f"Eats Meat?:\t{str(self.isCarnivore)}.")


	def make_noise(self):
		print(f"{self.name} says 'BLUB'.")


class Salmon(Fish):
	def __init__(self, name, species, fins, isCarnivore):
		super(Salmon, self).__init__(name, species, fins, isCarnivore)
		self.pattern = "Red Stripes"

	def print_info(self):
		super(Salmon, self).print_info()
		print(f"Pattern:\t{self.pattern}")

class Halibut(Fish):
	def __init__(self, name, species, fins, isCarnivore):
		super(Halibut, self).__init__(name, species, fins, isCarnivore)
		self.pattern = "Scales"

	def print_info(self):
		super(Halibut, self).print_info()
		print(f"Pattern:\t{self.pattern}.")

	# this function can only be called from Halibut objects, not from generic Fish objects
	def swim_fast(self):
		print(f"Halibut {self.name.title()} began swimming fast.")



rusty = Dog('Rusty')
rusty.make_sound()
rusty.move_around()

print("=" * 50)

maru = Cat("Maru")
maru.make_sound()
maru.move_around()

print("=" * 50)


print("=" * 50)
haley = Halibut("Haley", "Freshwater Halibut", "3", True)
haley.make_noise()
haley.print_info()
haley.swim_fast()


nemo = Salmon("Nemo", "Creek Salmon", "5", False)
nemo.make_noise()
nemo.print_info()
try:
	nemo.swim_fast()
except AttributeError:
	print("The attribute swim_fast is not defined for Nemo.")

print("""
Even when the functions are defined in the base classes, they can still be called
from the inheriting classes. make_noise and make_sound are both functions that are defined
for the superclasses Fish and Animal. This means both Cat and Dog inherit the make_sound
function while both Halibut and Salmon inherit the make_noise function. 

However, if a function is not defined in the superclass, then only the specific
class for which its defined can create instances which can use the function. For example,
the swim_fast method is defined only for Halibuts and not for Salmons. So when the Salmon
object nemo tries to access this function, it results in AttributeError that is caught
and handled with a try-catch block.
""")