"""This script opens the file to which we wrote three strings in ex16
And reads this new data to print to the console to show that the file's contents
have indeed changed.

This is also a common programming operation - files are commonly read, written to, and then 
read again by a programme.
"""

from sys import argv

script_name, file_name = argv

print(f"The script file {script_name} will read and echo data from {file_name}.")

target_file_obj = open(file_name)
print(target_file_obj.read())

target_file_obj.close()
