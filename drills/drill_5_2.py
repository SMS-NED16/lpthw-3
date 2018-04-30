name = 'Zed A. Shaw'
age = 35

height = 74 # inches
# Adding variable to convert weight in pounds to kg
height_cm = height * 2.54 # 1 inch = 2.54 cm

weight = 180 # lbs
# Adding variable to convert height in inches to centimetres
weight_kg = weight * 0.454 # 1 kg = 0.454 lb

eyes = 'Blue'
hair = 'Brown'
teeth = 'White'

print(f"Let's talk about {name}.")
print(f"He is {age} years old.")
print(f"He is {height} inches tall.")
print(f"That's about {round(height_cm)} centimetres tall.")
print(f"He is also {weight} pounds heavy.")
print(f"That's about {round(weight_kg)} in kilograms.")
print("Actually that's not too heavy.")
print(f"His eyes are {eyes} and his hair is {hair}.")
print(f"His teeth are usually {teeth}, depending on the coffee.")

