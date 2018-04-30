tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("I am 6'2\" tall.")	# escape double-quote inside string
print('I am 6\'2" tall.')	# escape single-quote inside string

# Testing all escape sequences
print("Testing \\ the \\ backslash.")
print("Testing the \'single quote\'.")
print("Testing the \"double quote\".")
print("Testing ASCII bell.\a")
print("Testing ASCII backspace\b.")
print("Testing ASCII formfeed\f.")
print("Testing ASCII newline.\nNew line.")
print("Testing \n{TAB}Hello.")
print("Testing carriage\r return.")
print("\tTesting \thorizontal \ttab.")
print("Testing\v vertical tab.")
print("16-bit hex \uFFFF.")
# print("32-bit hex \UFAFAFAFA.")
print("Testing octal \723.")
print("Hex value \xFF.")