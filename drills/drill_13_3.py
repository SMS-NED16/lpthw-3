# This drill mixes input with argv 
# INPUT - used to get input from the user at runtime, not necessarily from the command line
# ARGV - used to get input from the user before runtime i.e. at compile time, almost always from the command line

from sys import argv

script_name, arg_ip = argv
print("You just ran the Python script called", script_name)
name = input("What is your name? ")

print(f"You gave {len(argv)} inputs to this programme.")
print("The first one was a command line/argument variable input:", arg_ip)
print("The second one was a standard runtime input:", name)