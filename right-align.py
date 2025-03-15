# right aligning input of words
# 19 April 2022

strings = input("Enter strings (end with DONE):\n")

stringList = []                 # container for the list of names
stringList.append(strings)      # adds first name into the list
if strings == "DONE":
    print('\nRight-aligned list:')
else:
    while strings != "DONE":        # loops until DONE is entered
        strings = input("")         # prompts for more names
        stringList.append(strings)  # adds each input into list
    stringList.pop(-1)              # removes DONE from the list

    sortedList=[]                   # container for sorted list of names
    for word in stringList:         # finds the longest word
        sortedList.append((len(word),word)) # adds length of word with word to list
    sortedList.sort()               # sorts list in ascending order
    longestWord = len(sortedList[-1][1])    # gives length of the longest word

    print('\nRight-aligned list:')
    for words in stringList:        # aligns each word
        aligned = (f'{str(words):>{longestWord}}')
        print(aligned)