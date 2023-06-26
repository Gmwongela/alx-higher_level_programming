#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Function that divides 2 integers and prints the result
    Returns the value of the division, otherwise: None
    """
    try:
        res = a / b
    except:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
