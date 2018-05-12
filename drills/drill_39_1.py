"""Programme which uses dictionaries to store states and citites in Pakistan"""

# Dictionaries of states mapped to their abbreviations
states = {
	'Sindh': 'SN',
	'Punjab': 'PN',
	'Balochistan': 'BST',
	'Khyber Pakthunkhwa': 'KPK',
	'Islamabad and Capital Territories': 'ISB',
	'Federally Administered Tribal Areas': 'FATA',
}

# Dictionaries of cities mapped to each state
cities = {
	'SN' : ['Karachi', 'Hyderabad', 'Larkana'],
	'PN': ['Lahore', 'Multan', 'Faisalabad'],
	'BST': ['Quetta', 'Gwadar', 'Zhob'],
	'KPK': ['Peshawar', 'Mardan'],
	'ISB': ['Islamabad'],
	'FATA': ['Swat', 'Mianwali', 'Rahimyar Khan']
}

# print some states
print('-' * 20)
print("Sindh's abbreviation is: ", states['Sindh'])
print("Balochistan's abbreviation is: ", states['Balochistan'])

# print some cities
print('-' * 20)
print("SN state has: ", cities['SN'])
print("BST state has: ", cities['BST'])

# do it by using the state then cities dict
print('-' * 20)
print("Sindh has: ", cities[states['Sindh']])
print("Balochistan has ", cities[states['Balochistan']])

# print every state's abbrevation
print('-' * 20)
for state, abbrev in states.items():
	print(f"{state} is abbreviated {abbrev}.")

# print every city in state
print('-' * 20)
for state, city_list in cities.items():
	print(f"{state} has cities.")
	for city in city_list:
		print(f"\t- {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}.")
	print(f"and has the following cities.")
	for city in cities[abbrev]:
		print(f"\t- {city}")

# safely get abbrevation by state that might not be there
state = states.get('Muhajir Sooba')
if not state:
	print("Sorry, no Muhajir Sooba. Marsun Marsun, Sindh na desun")

# get a city with a default value
city = cities.get('Muhajir Sooba', 'Does not exist')
print(f"The city for the state 'Muhajir Sooba' is: {city}.")