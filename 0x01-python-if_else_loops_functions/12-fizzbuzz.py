#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            elem = "FizzBuzz"
        elif i % 3 == 0:
            elem = "Fizz"
        elif i % 5 == 0:
            elem = "Buzz"
        else:
            elem = i
        print("{}".format(elem), end=" ")
