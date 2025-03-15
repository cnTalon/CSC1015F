# Calculate value of PI
# 26 February 2022

import math

pie = round(2 * (2 / math.sqrt(2)) * (2 / (math.sqrt(2 + math.sqrt(2))) * (2 / (math.sqrt(2+ (math.sqrt(2 +(math.sqrt(2)))))))), 4)

print("Approximation of pi:", pie)

r = eval(input("Enter the radius:\n"))

area = round(pie * r ** 2 + + 0.0001, 4) 
print("Area:", area)