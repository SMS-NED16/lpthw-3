# Here's some new strange stuff, remembeer type it exactly.

# Create a string with abbreviated names of the days of the week
# All days are separated by a single space, will be printed on the same line
days = 'Mon Tue Wed Thu Fri Sat Sun'

# Create a string with abbreviated names of some months
# Separate names using the \ncharacter - special escape sequence
# Every time Python finds a \n, it prints the following text on a new line
months = 'Jan\nFeb\n\Mar\nApr\nMay\nJun\nJul\nAug'

# Printing days string after message
print("Here are the days: ", days)

# Printing months string after message
print("Here are the months: ", months)

# Printing a special string that is enclosed in double quotes
# It is different from conventional strings in that it is delimited by three
# pairs of double quotes, and that the string contents do not ignore whitespace
print("""
There's something going on here
With the three double-quotes
We'll be able to type as much as we like
Even 4 lines if we want, or 5, or 6.
""")