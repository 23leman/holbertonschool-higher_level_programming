#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the square

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Getter to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)
