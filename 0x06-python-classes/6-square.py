#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """ Represent a square """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if type(i) is not int:
                raise TypeError("position must be a tuple of\
                                2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of\
                            2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of\
                            2 positive integers")
        for i in position:
            if type(i) is not int:
                raise TypeError(self.tuple_error)
        self.__position = value

    def area(self):
        """ Return the current area of the square """
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        spaces = ' ' * self.__position[0]
        square_print = '#'
        if self.__size != 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print("{}{}".format(spaces, square_print * self.__size))
        else:
            print("")
