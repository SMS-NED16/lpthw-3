"""This programme demonstrates some of the operations that can be performed with dictionaries"""

# Create a dictionary of names and ages
people = {
	'Saad' : 22,
	'Mashkoor' : 63,
	'Nasreen' : 58,
}

print("Shallow copy")
print("""Creates a `shallow` copy of the dictionary argument provided.
I.e. creates a new dictionary with all the elements of the argument dictionary.
These are different dictionaries which occupy different addresses in memory. Only
their contents are the same, hence the name 'shallow copy.'
""")
people_2 = people.copy()
print("Contents of people dict")
print(people)
print("\nContents of people_2 dict.")
print(people_2)

print("-" * 50)

print("clear".upper())
print("""Removes all items from a dictionary. Not the same as deleting the 
dictionary itself. The dictionary will still persist in memory, only its items
will be deleted.""")
print("people_2 after clearing.")
people_2.clear()
print(people_2)	# empty dictionary

print("-" * 50)
print("fromkeys".upper())
print("""Takes an iterable data structure (list, tuple, string) as an argument.
Returns a new dictionary with the elements of the iterable as the keys of the dictionary,
and a predefined value argument as their value.""")
print("Creating a list of friends as an iterable for a new dict.")
list_of_names = ['Faiq', 'Fawad', 'Hasan', 'Haseeb', 'Waleed']	# an iterable
print(list_of_names)
print("Result of creating friends_dict = dict.fromkeys(list_of_names, 'Friend').")
friends_dict = dict.fromkeys(list_of_names, 'Friend')
print(friends_dict)

print("-" * 50)
print("get".upper())
print("""Returns the value of a key in a dictionary if key is present. Otherwise returns 'None'.
Allows the programme to run without errors even if a non-existent key is accessed.""")
print("Getting 'Saad' from people", people.get('Saad'))
print("Getting 'Johnny' from people.", people.get('Johnny'))	# Johnny isn't present in the dictionary

print("-" * 50)
print("items".upper())
print("""Returns a set-like object providing a view of the dictionary's key-value pairs.
A set is a data structure in which a value appears only once.""")
print(people.items())
print(friends_dict.items())

print("-" * 50)
print("keys".upper())
print("""Returns a set-like object with the keys of the dictionary.""")
print(people.keys())
print(friends_dict.keys())

print("-" * 50)
print("pop".upper())
print("""Looks for a specific key or key-value pair in a dictionary, removes it, and then 
returns the value removed. If the key is not found, the value passed as the argument is returned.
If no value was passed as an argument, KeyError is raised.""")
print(people.pop('Saad'))
print("People dict after removing saad", people)
# print(people.pop('Sugoi')) key error
print("People dict after removing Sugoi", people)

print("-" * 50)
print("popitem()".upper())
print("""Same as pop, but instead of returning the value of the key, returns a tuple representing
the key-value pair. Also returns the LAST key-value pair in the dictionary. The order of a dictionary
is not fixed,  so there is no guarantee that this will be a specific key-value pair.
If the dictionary is empty then dict.popitem() causes a KeyError.""")
print(people.popitem())
print("People dict after popitem", people)

print('-' * 50)
print("setdefault()".upper())
print("""Sets default-key value pairs for a dictionary.""")
people.setdefault('Saad', 21)
print(people)

print("-" * 50)
print("values".upper())
print("""An object providing a view on the values of the dictionary, not the keys.""")
print(people.values())
