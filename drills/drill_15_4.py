"""This version of the exercise 15 script removes lines 10 - 15 from the original script
i.e. the lines that were responsible for the user entering the name of the file at runtime."""

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}.")
print(txt.read())