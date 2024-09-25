#!/usr/bin/python3
"""Module: 4-inherits_from
"""

def inherits_from(obj, a_class):
    """The Object is an instance a_class
    that inherited(directly or indirectly)
    obj: an object
    a_class: a class
    Return: None
    """

    return type(obj) != a_class and
    isinstance(obj, a_class)
