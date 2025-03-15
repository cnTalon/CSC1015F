# adapted combined.py
# 2 April 2022

def get_integer(s):
    # collects the input
    p = s                               # sets the prompt variable to a set variable in case the input is invalid & will allow prompt to reissue the user input box
    s = input("Enter "+ s +":\n")
    while not s.isdigit():              # if not digit then asks again for digit
        s = input("Enter " + p+":\n")
    s = eval(s)
    if s < 0:
        s = input("Enter " + p +":\n")
    return s

def calc_factorial(n):
    # calculates the factorial
    nfactorial = 1
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial