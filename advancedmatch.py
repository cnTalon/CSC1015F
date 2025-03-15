# advanced matching with two types of wildcards
# 28 April 2022

def match(pattern, word):
    if pattern !="*":
        if pattern and word:        # checks to see if the two strings are not empty
            if pattern[0] == "?" or pattern[0] == word[0]:
                return match(pattern[1:], word[1:])
            elif pattern[0] == "*":       # checks if first char is * or if last chars are equal
                return match(pattern, word[1:]) or match(pattern[1:], word)
                
            return False
            
        elif not(pattern or word):
            return True             # base case: pattern & word are empty
        return False                # base case: either pattern or word is empty
    return True                     # base case: pattern is *