# Pythagoras's Theorem
# 26 February 2022

import math
a = eval(input("Enter the length of side a:\n"))
c = eval(input("Enter the length of side c:\n"))


if c < 0:
    print("Sorry, lengths must be positive numbers.")

if c > 0:
    if a > 0:

        theo = math.sqrt(c ** 2 - a ** 2)

        print("The length of side b is", theo, end='.')
    else:
        print("Sorry, lengths must be positive numbers.")
