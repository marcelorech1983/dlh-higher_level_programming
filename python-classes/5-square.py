#!/usr/bin/python3
"""This module represent a class called Square"""


class Square:
    """This class represents a Square."""
    def __init__(self, size=0):
        """inicialize with size"""
        self.size = size

    @property
    def size(self):
        """Return the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Define the size with validation"""
        if not isinstance(value, int):
            """Validate if the value is an integer"""
            raise TypeError("size must be an integer")
        if value < 0:
            """Validate if the value is greater or equals 0"""
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the calculated area."""
        return self.size ** 2

    def my_print(self):
        """Print the square with the character #"""
        if self.size == 0:
            """Print validation, if size = 0 print an empty line"""
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
