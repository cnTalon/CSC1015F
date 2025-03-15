# prints palindromic primes
# 28 April 2022

import math
import sys
sys.setrecursionlimit(30000)

def isPrime(n, integer):
    # verifies if prime
    if integer > math.sqrt(n):      # base case: integer larger than n and doesnt flag as not prime
        return True
    if n == 2:                      # base case: n is 2
        return True
    if not n % integer:             # base case: more factors than just 1 and itself for n
        return False
    if integer % 2:                 # if odd add 2 else add 1
        integer += 1
    return isPrime(n, integer + 1)

def isPalindrome(n):
    # same function from palindrome.py
    if len(n) <= 1:
        return True
    else:
        first, *rest = n        # selects the first letter
        if rest:
            *leftover, last = rest  # selects last letter
        if first == last:       # check if equal
            return isPalindrome(leftover) # if equal then recurse and check other letters
        else:
            return False

def palprime(n,m):
    # recurses through the range of numbers to determine if prime and palindrome
    if n <= m:
        if isPrime(n, integer):         # if prime check if palindrome otherwise go to next number
            if isPalindrome(str(n)):
                print(n)
        if n % 2:
            n += 1
        palprime(n + 1, m)

n = int(input("Enter the starting point N:\n"))
m = int(input("Enter the ending point M:\n"))
integer = int(2)

print("The palindromic primes are:")
palprime(n,m)