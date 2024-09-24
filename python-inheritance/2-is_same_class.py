#!/usr/bin/python3
# 2-is_same_class.py

"""Defines a class-checking function."""

def is_same_class(obj, a_class):
    """Check if and object is exactly an instance
     of a given class.
     Arg:
        obj (any): the object to check.
        a_class (type): The class to mathc the type of obj to.
        Returns.
            If obj is exactly an instance 
            of a_class - True.
                    otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
        