# importing a module - a predefined set of features
#  we can use to extend our python script's functionality
from sys import argv		# argv stands for `argument variable`

# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

explanation = """When we run Python code using the command line, it is usually with a line like this'python3.6 ex13.py'
The ex13.py is an argument to the python3.6 command - it is information that is passed to
the command to tell it which script to run. Every python3.6 call like this one can take 
an arbitrary number of argument variables that are stored in a list of variables called the `argv`
If we want to provide arguments to the script from the command line (as opposed to gettin info from
the user during runtime and passing that as arguments to some function), then we need to pass these 
arguments to the argv list and then unpack them during runtime. To do this, we first import the 'argv'
module from the 'sys' module. 'sys' is a collection of modules that are involved with interpreter interaction.
'argv' is one of these modules. It allows us to access the argv list of a Python script's execution call,
store these arguments in some variables and then use them. This is what is happening on line 6
The argv variable is unpacked, and each variable within it is stored in 'script', 'first', 'second', and then
'third' in that order.
The first argument will always be the name of the python script/file that is being executed.
"""