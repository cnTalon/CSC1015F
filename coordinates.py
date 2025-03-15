# is it a geographical pair
# 3 March 2022

latd = eval(input("Enter first number:\n"))
latm = eval(input("Enter second number:\n"))
lats = eval(input("Enter third number:\n"))
lond = eval(input("Enter fourth number:\n"))
lonm = eval(input("Enter fifth number:\n"))
lons = eval(input("Enter sixth number:\n"))

if latd >= -90 and latd <= 90:
    if latm >=0 and latm <=59:
        if lats >=0 and lats <=59:
            if lond >= -180 and lond <= 180:
                if lonm >= 0 and lonm <= 59:
                    if lons >= 0 and lons <= 59:
                        print("WOW! Looks like geographic coordinates!")
                    else:
                        print("Hmmm ... looks like 6 random numbers.")
                else:
                    print("Hmmm ... looks like 6 random numbers.")
            else:
                print("Hmmm ... looks like 6 random numbers.")
        else:
            print("Hmmm ... looks like 6 random numbers.")
    else:
        print("Hmmm ... looks like 6 random numbers.")
else:
    print("Hmmm ... looks like 6 random numbers.")