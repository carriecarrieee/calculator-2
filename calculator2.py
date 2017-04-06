"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

calc_file = open("calculations.txt")
    

for each_command in calc_file:        # loop through lines of commands
    each_command = each_command.rstrip()
    print each_command

    try:          # if user enters invalid entry or errors, will print except statement
        tokens = each_command.split(" ")
        operator = tokens[1]
        num_list = tokens[::2]
        if operator == "+":
            print "%.2f\n" % reduce(lambda x, y: int(x) + int(y), num_list)
        elif operator == "-":
            print "%.2f\n" % reduce(lambda x, y: int(x) - int(y), num_list)
        elif operator == "*":
            print "%.2f\n" % reduce(lambda x, y: int(x) * int(y), num_list)
        elif operator == "/":
            print "%.2f\n" % reduce(lambda x, y: int(x) / int(y), num_list)
        elif operator == "square":
            print "%.2f\n" % reduce(lambda x: int(x) ** 2, num_list[0])
        elif operator == "cube":
            print "%.2f\n" % reduce(lambda x: int(x) ** 3, num_list[0])
        elif operator == "pow":
            print "%.2f\n" % reduce(lambda x, y: int(x)**int(y), num_list)
        elif operator == "mod":
            print "%.2f\n" % reduce(lambda x, y: int(x) % int(y), num_list)
        else:
            print "Invalid entry, please try again!"
    except:
        print "Invalid entry, please try again."
