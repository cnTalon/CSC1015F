# hollow star box functions
# 2 April 2022

import math

def print_square():                                     # printing a 5x5 square
    square = ''
    for a in range(0,5):
        for b in range(0,5):
            if a == 0 or a == 4 or b==0 or b==4:
                square += "* "                          # stores stars
            else:
                square += "  "                          # stores spaces
        if a != 4:                                      # stops printing newline after shape
            square += "\n"
    return square

def print_rectangle(width, height):                     # print a custom rectangle
    for h in range(0, height):
        for w in range(0, width):
            if w == 0 or w == width-1 or h == 0 or h == height-1:   # prints the rectangle outline
                print("* ", end='')
            else:
                print("  ", end='')                     # prints the blank space inside
        print()

def get_rectangle(width, height):                       # print type 2 custom rectangle
    result = ''
    for h in range(0, height):
        for w in range(0, width):
            if w == 0 or w == width-1 or h == 0 or h == height-1:
                result +="* "                           # stores stars
            else:
                result += "  "                          # stores spaces
        if h != height-1:
            result += "\n"                              # stops printing newline after shape
    return result

if __name__ == '__main__':
   main()        