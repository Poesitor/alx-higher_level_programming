#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10
if last_digit > 5:
    num_status = "and is greater than 5"
elif last_digit == 0:
    num_status = "and is 0"
else:
    num_status = "and is less than 6 and not 0"

print(f"Last digit of {number:d} is {last_digit:d} {num_status}")
