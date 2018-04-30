# Asks user for data and prints result to console
name = input("What is your name? ")
age = input("How old are you? ")
place_of_birth = input("Where were you born? ")
date_of_birth = input("When were you born? ")
fav_band = input("What is your favourite band? ")
fav_food = input("What is your favourite food? ")

# Print data back to user
print(f"This is all we know so far about {name.upper()}.")
print(f"{name.split(' ')[0]} was born in {place_of_birth} on {date_of_birth}.")
print(f"{name.split(' ')[0]}'s favourite band is {fav_band}.")
print(f"{name.split(' ')[0]} also loves to eat {fav_food}.")