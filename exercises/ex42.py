## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal i.e. Dog inherits from Animal class
class Dog(Animal):

	def __init__(self, name):
		# Instance of dog referred to by 'self' has-a name attribute
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		# Instance of Cat referred to by 'self' has-a name attribute
		self.name = name

#
class Person(object):

	def __init__(self, name):
		# Instance of Person referred to by 'self' has-a name attribute
		self.name = name;
		# Person has-a Pet of some kind
		self.pet = None

## Employee is-a Person i.e. Employee inherits from Person class
class Employee(Person):

	def __init__(self, name, salary):
		"""Initialises the Employee object by calling the superclass constructor""" 
		super(Employee, self).__init__(name)
		"""Then initialises the attributes specific to Employees that were absent in Person"""
		self.salary = salary

## A Fish is-a Object i.e. inehtis from the proto class object - all classes inherit from object
class Fish(object):
	pass

## A Salmon is-a Fish
class Salmon(Fish):
	pass

## A Halibut is-a Fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog('Rover')

## satan is-a Cat
satan = Cat('Satan')

## Mary is-a Person
mary = Person('Mary')

## Mary has-a Pet
mary.pet = satan

## Frank is-a Employee; has-a name Frank, has-a salary 120k
frank = Employee("Frank", 1200000)

## frank has-a pet i.e. Rover who is-a dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon which is-a Fish
crouse = Salmon()

## harry is-a Halibut which is-a Fish
harry = Halibut()
