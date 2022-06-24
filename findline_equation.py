""" Program for finding a line euation in standard form (Ax+By=C) from two points
    in cartisian co-ordinate form"""

from fractions import Fraction
import math
import sys


def err_get_input_again():
    """ method to show error message and ask user to either reinput values
    or exit program"""

    opt = input("Do you want to re-enter values? y/n ")
    opt = opt.lower()
    match opt:
        case 'y':
            input_coordinates()
        case 'n':
            sys.exit()
        case _:
            print("Please, enter either y or n")
            err_get_input_again()

def check_input(input_val):
    """ Check if input is number"""
    try:
        # Convert it into integer
        input_val.isdigit()
        return 1
    except ValueError:
        try:
            # Convert it into float
            float(input_val)
            return 1
        except ValueError:
            print("Input is not a number.\nFollow the instructions for providing input correctly!")
            show_input_instructions()
            return 0

def show_input_instructions():
    """ The method to print instructions for user about how to input co-ordinates correctly"""
    print("\n---- INPUT INSTRUCTIONS -----")
    print("Enter co-ordinates values separated by a comma:")
    print("For example co-ordinate (4,3) would be entered as: 4,3\n")

def input_coordinates():
    """ method to get co-ordinates from user"""
    show_input_instructions()

    coordinates = []
    try:
        x_1, y_1 = input("Enter first co-ordinate").split(',')
        if check_input(x_1) and check_input(y_1):
            coordinates.append(x_1)
            coordinates.append(y_1)
            print("P1: (" + x_1 + "," + y_1 + ")")
        else:
            err_get_input_again()
    except ValueError:
        print("\nPlease, follow the instructions for providing input correctly!")
        show_input_instructions()
        err_get_input_again()
        return coordinates

    try:
        x_2, y_2 = input("Enter second co-ordinate").split(',')
        if check_input(x_2) and check_input(y_2):
            coordinates.append(x_2)
            coordinates.append(y_2)
            print("P2: (" + x_2 + "," + y_2 + ")")
            print(coordinates)
            return coordinates
        else:
            err_get_input_again()
    except ValueError:
        print("\nPlease, follow the instructions for providing input correctly!")
        show_input_instructions()
        err_get_input_again()
    return coordinates

def convert_decimal_to_fraction(a,b,c):
    """ method to convert floating point co-efficients to fractions"""
    if  isinstance(a, float):
        a = Fraction(a).limit_denominator()
    if  isinstance(b, float):
        b = Fraction(b).limit_denominator()
    if  isinstance(c, float):
        c = Fraction(c).limit_denominator()
    return a,b,c

def find_gcf(a,b,c):
    """" method to find greatest common factor of co-effeicents"""
    common_factor = math.gcd(math.gcd(a,b),c)
    a = a // common_factor
    b = b // common_factor
    c = c // common_factor
    return a,b,c


def find_line_from_two_coordinates(lst):
    """ method to find the stand form of line from two cartisian cordinate pairs
    (x1,y1), (x2,y2) """
    numlst = []
    for item in lst:
        if item.isdigit():
            numlst.append(int(item))
        else:
            numlst.append(float(item))
    a = numlst[1] - numlst[3]
    b = numlst[2] - numlst[0]
    c = a*(numlst[0]) + b*(numlst[1])

    a,b,c = convert_decimal_to_fraction(a,b,c)
    
    if a == 0:
        opt = str(Fraction(b))+ " y = "+ str(Fraction(c))
    elif b == 0:
        opt = str(Fraction(a))+ "x = "+ str(Fraction(c))
    else:
        opt = str(Fraction(a))+ " x + "+ str(Fraction(b))+ " y = "+ str(Fraction(c))

    return opt