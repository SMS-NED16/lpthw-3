myString = """This is a \nstring that mixes {} with \v escape characters
to create {}.\n\t* It is important to know how to {} multiple programming tools
to \\ create {}."""

print(myString.format('format string techniques', 'complex formats', 
'mix and match', 'new solutions'))

name = 'Saad Mashkoor Siddiqui'
age = 21
hobby_1 = 'programming'
hobby_2 = 'eating pizza'
fav_band = 'AC/DC, not AC\\DC!'
print(f"Presenting data for {name}.\v* Age : {age}\nHobbies:\v *{hobby_1}\v*{hobby_2}\nFavourite Band: {fav_band}")