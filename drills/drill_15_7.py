"""This version of the ex15.py script uses the close() method to close
both input files after their read operation has been completed. Closing a file
is important because it prevents the files from accidentally being corrupted or overwritten
after their read operation/write operation has been completed"""


from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}.")
print(txt.read())
txt.close()		# closing the txt file after read operation has finished

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()	# closing the txt_Again file after read operation has finished