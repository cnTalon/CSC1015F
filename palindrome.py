# is it a palindrome?
# 25 April 2022

def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        first, *rest = s        # selects the first letter
        if rest:
            *leftover, last = rest  # selects last letter
        if first == last:       # check if equal
            return palindrome(leftover) # if equal then recurse and check other letters
        else:
            return False

def main():
    s = input("Enter a string:\n")
    if palindrome(s) == True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")

main()