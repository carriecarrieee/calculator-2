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
    num_list = tokens[1:len(tokens)]
    if operator == "+":
        print add(num_list)
    elif operator == "-":
        print subtract(num_list)
    elif operator == "*":
        print multiply(num_list)
    elif operator == "/":
        print divide(num_list)
    elif operator == "square":
        print square(num_list)
    elif operator == "cube":
        print cube(num_list)
    elif operator == "pow":
        print power(num_list)
    elif operator == "mod":
        print mod(num_list)
    else:
        print "Invalid entry, please try again."
