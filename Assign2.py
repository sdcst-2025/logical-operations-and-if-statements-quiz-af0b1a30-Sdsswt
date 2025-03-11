"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math

x = float(input("enter a number "))
y = float(input("enter a number "))

ans = input("are one of the numbers the hypotenuse of a right triangle? ")
ans = str(ans)
if ans == "yes":
    ms = math.sqrt((x**2) - (y**2))
    ms = round(ms)
    print(f"{ms} is the missing side length")
elif ans =="no":
    h = math.sqrt((x**2) + (y**2))
    h = round(h)
    print(f"{h} is the hypotenuse")
elif ans !="yes" or "no":
    print("your anwser has to be yes or no")
    exit()