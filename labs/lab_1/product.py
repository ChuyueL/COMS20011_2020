from __future__ import print_function

import sys

def product(numbers):
    """Function to return the product of two numbers
    Params:
        numbers: List of two numbers to be multiplied
    Returns:
        product of two numbers
    """
    #Write your solution here
    prod = int(numbers[0]) * int(numbers[1])
    print(prod)
    return prod

numbers = sys.argv[1:] # sys.argv contains the arguments passed to the program
product(numbers)
