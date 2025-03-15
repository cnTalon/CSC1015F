# converting gumatj to decimal vice versa, and performing mathematical operations
# 11 April 2022

def gumatj_to_decimal(a):
    if a % 10 == 0:
        if a < 100:
            decimal = int((a/10)*5)
        elif a >=100 and a <1000:
            decimal = int(a/4)
        else:
            decimal = int(a/8)
        return decimal
    elif a % 10 != 0:
        decimal = int((a//10)*5)
        base5 = decimal             # stores the decimal for further use
        remainder = a - decimal*2   # checks for the remainder after converting the gumatj from base5
        decimal = base5 + remainder # produces the decimal value
        return decimal

def decimal_to_gumatj(a):
    if a % 5 == 0:                  # checks if input has no remainder
        if a < 100:
            gumatj = int(a*4)
        elif a >=100 and a <625:
            gumatj = int(a*8)
        else:
            gumatj = int(a*16)
        return gumatj
    elif a % 10 != 0:
        gumatj = int((a//5)*10)
        base5 = gumatj              # saves the gumatj value for further use
        remainder = a - gumatj/2    # checks for the remainder after converting the decimal from base5
        gumatj = base5 + remainder  # produces gumatj value
        return int(gumatj)
    
def gumatj_add(a,b):
    if a % 10 == 0:                 # convert the gumatj to decimal form
        if a < 100:
            decimal = int((a/10)*5)
        elif a >=100 and a <1000:
            decimal = int(a/4)
        else:
            decimal = int(a/8)
    elif a % 10 != 0:
        decimal = int((a//10)*5)
        base5 = decimal             # save the decimal for further use
        remainder = a - decimal*2   # checks for remainder
        decimal = base5 + remainder # produces decimal value
    if b % 10 == 0:
        if b < 100:
            decimal2 = int((b/10)*5)
        elif b >=100 and b <1000:
            decimal2 = int(b/4)
        else:
            decimal2 = int(b/8)
    elif b % 10 != 0:
        decimal2 = int((b//10)*5)
        base5b = decimal2               # stores the second value for further use
        remainderb = b - decimal2*2     # checks for remainder
        decimal2 = base5b + remainderb  # produces second decimal value
    decimal = decimal + decimal2        # perform the math
    if decimal % 5 == 0:                # convert the answer back to gumatj
        if decimal < 100:
            gumatj = int(decimal*4)
        elif decimal >=100 and decimal <625:
            gumatj = int(decimal*8)
        else:
            gumatj = int(decimal*16)
        return gumatj
    elif decimal % 10 != 0:
        gumatj = int((decimal//5)*10)
        base5 = gumatj
        remainder = decimal - gumatj/2
        gumatj = base5 + remainder
        return int(gumatj)

def gumatj_multiply(a,b):
    product = a *b
    if product % 5 == 0:               # converts gumatji to appropriate gumatj value after math  
        if a < 100:
            gumatj = int(product*4)
        elif product >=100 and product <625:
            gumatj = int(product*8)
        else:
            gumatj = int(product*16)
        return gumatj
    elif product % 10 != 0:
        gumatj = int((product//5)*10)
        base5 = gumatj
        remainder = product - gumatj/2
        gumatj = base5 + remainder
        return int(gumatj)