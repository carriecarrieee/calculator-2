def add(num_list):
    """Return the sum of two numbers"""
    total = 0
    for item in num_list:
        total += int(item)
    return total

def subtract(num_list):
    """Return the difference of two numbers"""
    total = 2*int(num_list[0])
    for item in num_list:
        total -= int(item)
    return total

def multiply(num_list):
    """Return the product of two numbers"""
    total = 1
    for item in num_list:
        total *= int(item)
    return total

def divide(num_list):
    """Return the quotient of two numbers as a float"""
    total = float(num_list[0])**2
    for item in num_list:
        total /= float(item)
    return total

def square(num_list):
    """Return the square of a number"""
    return int(num_list[0]) ** 2

def cube(num_list):
    """Return the cube of a number"""
    return int(num_list[0]) ** 3

def power(num_list):
    """Return num raised to the power of exponent"""
    return int(num_list[0]) ** int(num_list[1])

def mod(num_list):
    """Return remainder of num1 divided by num2"""
    return int(num_list[0]) % int(num_list[1])
