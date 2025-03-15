# printing days of a month
# 13 March 2022

mm = input("Enter the month ('January', ..., 'December'):\n")
day = input("Enter the start day ('Monday', ..., 'Sunday'):\n")

space = ' '
days = "Mo Tu We Th Fr Sa Su"
print(mm)
print(days)
if mm == "January" or mm=="March" or mm=="May" or mm=="July" or mm=="August" or mm=="October" or mm=="December":
    if day =="Monday":
        for d in range(0, 31):              # number of days in month
            d += 1                          # starts off at 1
            if d >= 1 and d <10:            
                print("", d, end=' ')       # spaces for single digits
                if (d) % 7 ==0:
                    print()                 # ensures next row
            else:
                print(d, end=' ')           # leaves double digits
                if (d) % 7 ==0:
                    print()
    if day == "Tuesday":
        for d in range(-1, 31):
            if d < 0:                       # makes sure anything less than one isnt printed
                print("",space, end=' ')
            else:    
                d += 1
                if d >= 1 and d <10:
                    print("", d, end=' ')
                    if (d+1) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+1) % 7 ==0:
                        print()
    if day == "Wednesday":
        for d in range(-2, 31):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+2) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+2) % 7 ==0:
                        print()
    if day == "Thursday":
        for d in range(-3, 31):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+3) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+3) % 7 ==0:
                        print()
    if day == "Friday":
        for d in range(-4, 31):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+4) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+4) % 7 ==0:
                        print()
    if day == "Saturday":
        for d in range(-5, 31):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+5) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+5) % 7 ==0:
                        print()
    if day == "Sunday":
        for d in range(-6, 31):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+6) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+6) % 7 ==0:
                        print()
if mm == "April" or mm == "June" or mm=="September" or mm=="November":
    if day =="Monday":
        for d in range(0, 30):
            d += 1
            if d >= 1 and d <10:
                print("", d, end=' ')
                if (d) % 7 ==0:
                    print()
            else:
                print(d, end=' ')
                if (d) % 7 ==0:
                    print()
    if day == "Tuesday":
        for d in range(-1, 30):
            if d < 0:
                print("",space, end=' ')
            else:    
                d += 1
                if d >= 1 and d <10:
                    print("", d, end=' ')
                    if (d+1) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+1) % 7 ==0:
                        print()
    if day == "Wednesday":
        for d in range(-2, 30):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+2) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+2) % 7 ==0:
                        print()
    if day == "Thursday":
        for d in range(-3, 30):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+3) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+3) % 7 ==0:
                        print()
    if day == "Friday":
        for d in range(-4, 30):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+4) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+4) % 7 ==0:
                        print()
    if day == "Saturday":
        for d in range(-5, 30):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+5) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+5) % 7 ==0:
                        print()
    if day == "Sunday":
        for d in range(-6, 30):
            if d <0:
                print("",space, end=' ')
            else:
                d += 1
                if d >= 0 and d <10:
                    print("", d, end=' ')
                    if (d+6) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d+6) % 7 ==0:
                        print()
else:
    if mm=="February":
        if day =="Monday":
            for d in range(0, 28):
                d += 1
                if d >= 1 and d <10:
                    print("", d, end=' ')
                    if (d) % 7 ==0:
                        print()
                else:
                    print(d, end=' ')
                    if (d) % 7 ==0:
                        print()
        if day == "Tuesday":
            for d in range(-1, 28):
                if d < 0:
                    print("",space, end=' ')
                else:    
                    d += 1
                    if d >= 1 and d <10:
                        print("", d, end=' ')
                        if (d+1) % 7 ==0:
                            print()
                    else:
                        print(d, end=' ')
                        if (d+1) % 7 ==0:
                            print()
        if day == "Wednesday":
            for d in range(-2, 28):
                if d <0:
                    print("",space, end=' ')
                else:
                    d += 1
                    if d >= 0 and d <10:
                        print("", d, end=' ')
                        if (d+2) % 7 ==0:
                            print()
                    else:
                        print(d, end=' ')
                        if (d+2) % 7 ==0:
                            print()
        if day == "Thursday":
            for d in range(-3, 28):
                if d <0:
                    print("",space, end=' ')
                else:
                    d += 1
                    if d >= 0 and d <10:
                        print("", d, end=' ')
                        if (d+3) % 7 ==0:
                            print()
                    else:
                        print(d, end=' ')
                        if (d+3) % 7 ==0:
                            print()
        if day == "Friday":
            for d in range(-4, 28):
                if d <0:
                    print("",space, end=' ')
                else:
                    d += 1
                    if d >= 0 and d <10:
                        print("", d, end=' ')
                        if (d+4) % 7 ==0:
                            print()
                    else:
                        print(d, end=' ')
                        if (d+4) % 7 ==0:
                            print()
        if day == "Saturday":
            for d in range(-5, 28):
                if d <0:
                    print("",space, end=' ')
                else:
                    d += 1
                    if d >= 0 and d <10:
                        print("", d, end=' ')
                        if (d+5) % 7 ==0:
                            print()
                    else:
                        print(d, end=' ')
                        if (d+5) % 7 ==0:
                            print()
        if day == "Sunday":
            for d in range(-6, 28):
                if d <0:
                    print("",space, end=' ')
                else:
                    d += 1
                    if d >= 0 and d <10:
                        print("", d, end=' ')
                        if (d+6) % 7 ==0:
                            print()
                    else:
                        print(d, end=' ')
                        if (d+6) % 7 ==0:
                            print()