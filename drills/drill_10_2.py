# Experimenting with triple-single-quote
print("""
This message is printed between triple double-quotes.
It allows us to write as many lines as we want as a single string literal.
Whitespace is not ignored in such a string, so a new line in the text editor
Also means a new line in the final Python output string.
""")

print('''
This message is printed between triple single-quotes.
How is it any different from the triple double-quotes?
Reading reading reading lorem ipsum.
''')

print('''
	Testing if the triple single-quotes ignore whitespace
	If it does, then it's not the same as using triple double quotes.
''')

print('''
The only reason for using single triple-quotes like in this string
Is if the string contains "double quotes like these" and you don't want to 
use escape sequences.
''')