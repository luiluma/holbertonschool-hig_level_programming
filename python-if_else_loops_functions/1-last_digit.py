#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
#if number < 0:
    #lastDigit = -lastDigit
#else:
    #lastDigit = number % 10

print(f"las digit of {number} is {lastDigit} and is", end=" ")

if lastDigit > 5:
    print("greater than 5")
elif lastDigit == 0:
    print("0")
elif lastDigit < 6:
    print("less than 6 and not 0")
