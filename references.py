# referencing program
# 22 March 2022

inp = input("Enter the reference:\n")

Author = inp.find(")")+2                    
Author2 = inp[:Author]                      # finds the author and the year
Author2 = Author2.title()                   # capitalises each first letter of the author(s)

pos = inp.index(",")
pos = inp.index(",", inp.index(",")+pos)    # finds the position of title of the reference

title2 = inp[Author:pos+2]                  # finds the title of the reference
title3 = title2.capitalize()                # sets it so that only the first letter of the title is capitalised

rest = inp[pos+2:]                          # adds in the rest of the reference
print("Reformatted reference:\n"+Author2 + title3 + rest)