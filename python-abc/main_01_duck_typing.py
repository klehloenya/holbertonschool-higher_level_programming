#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

# Instantiate Dog and Cat objects
bobby = Dog()
garfield = Cat()

# Print the sounds they make
print(bobby.sound())  # Output: Bark
print(garfield.sound())  # Output: Meow

# Attempting to instantiate Animal will raise a TypeError
try:
    animal = Animal()  # This will raise an error
except TypeError as e:
    print(e)  # Output: Can't instantiate abstract class Animal with abstract method sound
