# counting pairs of letters
# 25 April 2022

def pairs(user):
    if len(user) >= 2:
        first, *rest = user             # selects the first letter from string
        if rest:
            second, *leftover = rest    # selects second letter from string
            if first == second:         # checks if they match
                return 1 + pairs(leftover)  # if match then add one and recurse
            return pairs(rest)          # if no match, recurse and dont add one
    return 0

def main():
    user = input("Enter a message:\n")
    num = pairs(user)
    print("Number of pairs:", num)

if __name__ == '__main__':
    main()