"""This is a simplified verssion of the ex17.py file that removes
extra features like checking if a file exists and reduces output to the screen"""

from sys import argv

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)
in_file_data = in_file.read()

out_file = open(to_file, 'w')
out_file.write(in_file_data)

in_file.close()
out_file.close()
print("Copying operation complete.")