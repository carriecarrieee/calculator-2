"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
new_input = ""
while new_input != "q":
    new_input = raw_input("> ")
    tokens = new_input.split(" ")
    operator = tokens[0]
    first_number = int(tokens[1])
    sec_number = int(tokens[2])
    # LATER: check to make sure user input valid
    if tokens[0] == "+":
        print add(first_number, sec_number)