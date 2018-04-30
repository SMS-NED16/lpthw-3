err_message = """python3.6 ex13.py 
Traceback (most recent call last):
  File "ex13.py", line 6, in <module>
    script, first, second, third = argv
ValueError: not enough values to unpack (expected 4, got 1)"""

print("Error message is\n", err_message)
explanation = """"The way we've written our Python script for exercise 13 means that
the argument variable for an execution call of this script MUST HAVE 4 VALUES. If we provide
any more or any less, then Python will throw an error telling us that it expected a certain number
of arguments to be passed to the Python script before execution, and how many it actually got.
""""