# matching words with wildcards
# 25 April 2022

def match(pattern, word):
    if len(pattern) == len(word):
        if pattern and word:        # checks to see if the two strings are not empty
            first, *rest = pattern  # first letter of pattern input
            firstL, *restL = word   # first letter of word input
            if first == "?" or first == firstL:
                return match(rest, restL)
        elif not(pattern or word):
            return True             # base case: pattern & word are empty
        return False                # base case: either pattern or word is empty
    return False                    # base case: pattern and word hae different lengths