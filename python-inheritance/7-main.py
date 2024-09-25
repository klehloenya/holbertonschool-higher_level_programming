#!/usr/bin/python3
# 7-main.py
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)  # This should pass
bg.integer_validator("width", 89)  # This should pass

try:
    bg.integer_validator("name", "John")  # Raises a TypeError
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)  # Raises a ValueError
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)  # Raises a ValueError
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
