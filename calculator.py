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

    try:
        tokens = new_input.split(" ")
        operator = tokens[0]
        num_list = tokens[1:len(tokens)]
        if operator == "+":
            print "%.2f" % add(num_list)
        elif operator == "-":
            print "%.2f" % subtract(num_list)
        elif operator == "*":
            print "%.2f" % multiply(num_list)
        elif operator == "/":
            print "%.2f" % divide(num_list)
        elif operator == "square":
            print "%.2f" % square(num_list)
        elif operator == "cube":
            print "%.2f" % cube(num_list)
        elif operator == "pow":
            print "%.2f" % power(num_list)
        elif operator == "mod":
            print "%.2f" % mod(num_list)
        else:
            print "Invalid entry, please try again."
    except:
        print "Invalid entry, please try again."
