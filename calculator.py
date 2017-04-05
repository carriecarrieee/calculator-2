"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    new_input = raw_input("> ")

    if new_input == "q":
        break

    tokens = new_input.split(" ")
    operator = tokens[0]
    first_number = int(tokens[1])
    sec_number = int(tokens[2])

    if operator == "+":
        print add(first_number, sec_number)
    elif operator == "-":
        print subtract(first_number, sec_number)
    elif operator == "*":
        print multiply(first_number, sec_number)
    elif operator == "/":
        print divide(first_number, sec_number)
    elif operator == "square":
        print square(first_number, sec_number)
    elif operator == "cube":
        print cube(first_number, sec_number)
    elif operator == "pow":
        print power(first_number, sec_number)
    elif operator == "mod":
        print mod(first_number, sec_number)
    else:
        print "Invalid entry, please try again."

