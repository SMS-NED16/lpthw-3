"""This version of the ex15 script uses only the `input()` function
to get the filename from the user instead of using an argument variable"""

print("Enter the name or filepath of the input file.")
file_name = input("> ")

if open(file_name):
	print(open(file_name).read())
else:
	print("Could not open input file.")
print("END OF PROGRAMME")

print("When to use the argv method".upper())
print("""
Using a command line argument to pass the name of the input file to a Python script is a better solution for applications in which multiple files have to be opened,
read, and closed quickly. It is possible to write a script that will pass a list of file names to the python3.6 command one by one i.e. automating the file reading process, in which case the 
argument variable method is best. \nAs a programmer, this method allows us to make our programme more robust in that there is less likelihood
of the wrong filepath or file name being entered by the user. \nHowever, this method is only useful if we know which files are to be opened ahead of time i.e. before runtime.
""")

print("When to use the user input method?".upper())
print("""
\nWhen we don't know which file a user would like to open ahead of time (such as in a photo sharing application), \nthe input method is better than the argv method. While it does carry the risk of the user entering an incorrect filename,
it is still a more interactive way of incorporating file input in to the programme.
""")