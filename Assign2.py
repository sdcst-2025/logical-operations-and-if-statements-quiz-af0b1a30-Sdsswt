"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

import math


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))


is_hypotenuse = input("Is one of these the hypotenuse? yes/no: ").lower()

if is_hypotenuse == "yes":
    hypotenuse = max(a, b)
    other_side = min(a, b)
    missing_side = math.sqrt(hypotenuse**2 - other_side**2)
else:
    missing_side = math.sqrt(a**2 + b**2)


print(f"The missing side is {round(missing_side, 1)}")

