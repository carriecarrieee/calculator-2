"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

calc_file = open("calculations.txt")
    

for each_command in calc_file:        # loop through lines of commands
    each_command = each_command.rstrip()
    print each_command

    try:          # if user enters invalid entry or errors, will print except statement
        tokens = each_command.split(" ")
        operator = tokens[0]
        num_list = tokens[1:]
        if operator == "+":
            print "%.2f\n" % add(num_list)
        elif operator == "-":
            print "%.2f\n" % subtract(num_list)
        elif operator == "*":
            print "%.2f\n" % multiply(num_list)
        elif operator == "/":
            print "%.2f\n" % divide(num_list)
        elif operator == "square":
            print "%.2f\n" % square(num_list)
        elif operator == "cube":
            print "%.2f\n" % cube(num_list)
        elif operator == "pow":
            print "%.2f\n" % power(num_list)
        elif operator == "mod":
            print "%.2f\n" % mod(num_list)
        else:
            print "Invalid entry, please try again!"
    except:
        print "Invalid entry, please try again."
