#!/usr/bin/python3
"""Define a class square"""

class square:
    """Represent a square"""

    def __inti__(self, size = 0):
        """Initialize a square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
