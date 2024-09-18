#!/usr/bin/python3
"""Define a class square"""

class Square:
    """Represent a square"""

    def __int__(self, size=0):
        """Initialise a new source.
        
        Args:
            size (int): The ize of the new square.
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(Self):
            """Return the current area of the square."""

            return (self.__size * self. __size)

        