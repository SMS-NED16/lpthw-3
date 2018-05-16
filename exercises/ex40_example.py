# importing a module i.e. a collection of functions and variab
import ex40_mystuff

# creating a dictionary and accesing a key-value pair
mystuff = {'apple': 'I AM APPLES! [from the  dictionary]'}
print(mystuff['apple'])

# accessing function from module with dot operator
ex40_mystuff.apple()

#accessing variable from module with dot operator
print(ex40_mystuff.tangerine);

print(mystuff['apple'])			# get apple from the dictionary
ex40_mystuff.apple()			# get aple from the module
print(ex40_mystuff.tangerine)	# same thing, it's just a variableb

# creating a class
class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)