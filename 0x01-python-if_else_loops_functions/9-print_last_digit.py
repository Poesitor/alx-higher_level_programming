#!/usr/bin/python3


def print_last_digit(number):
    """Prints the last digit of a number"""
    number = abs(number)
    print("{}".format(number % 10), end="")
    return (abs(number % 10))
