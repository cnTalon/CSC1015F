# drawing a function
# 22 March 2022

import math

func = input("Enter a function f(x):\n")

for y in range(10,-11,-1):          # sets the y axis
    for x in range(-10,11):         # sets the x axis
        fx = round(eval(func))      # gets the y values
        if y == fx:                 # prints the points
            print("o", end='')
        elif x == 0 and y == 0:     # prints origin
            print("+", end='')
        elif x == 0:                # prints y axis
            print("|", end='')
        elif y == 0:                # prints x axis
            print("-", end='')
        else:                       # prints blanks
            print(" ", end='')
    print()
