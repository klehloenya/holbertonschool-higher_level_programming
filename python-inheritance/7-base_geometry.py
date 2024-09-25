#!/usr/bin/python3
"""Represent a base geometry"""

def area(self):
    """Not yet implemented."""
    raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """validate a parameter for an integer:
    Args:
        name (str): The name of the parameter.
        
            value (int): The parameter of the 
            validate.
                Raise:
                    TypeError: If value is not an integer.
                                ValueError: If value is <= 0
                                """
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <=0:
        raise ValueError("{} must be greater than 0".format(name))
