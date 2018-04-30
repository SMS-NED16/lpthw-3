# This script takes more arguments than ex13.py
from sys import argv

print("Executing drill 13_2_b - More Arguments")

# Unpacking argv variable and storing contents in separate vars
script_name, first, second, third, fourth, fifth = argv

# Printing contents of argv
print("The script's name is:", script_name)
print("The first argument is:", first)
print("The second argument is:", second)
print("The third argument is:", third)
print("The fourth argument is:", fourth)
print("The fifth argument is:", fifth)