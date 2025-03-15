# finding anagrams of a word
# 8 May 2022

wordList = []
anagram = []

def frequency(word):        # gets frequency of all letters in word
    splitWord = {}
    for letter in set(word):
        splitWord[letter] = word.count(letter)
    return splitWord

print("***** Anagram Finder *****")
try:
    file = open("EnglishWords.txt", "r")

except FileNotFoundError as errno:   # if file is non-existent
    print("Sorry, could not find file", "'EnglishWords.txt'.")
else:
    word = input("Enter a word: ")
    word = word.lower()
    for line in file:
        if "START" in line:             # finds the beginning of the word list
            for line in file:
                line = line[:-1]        # removes the "\n" char
                if line != word and (frequency(word) == frequency(line)):   # checks if anagram
                    anagram.append(line)
    anagram.sort()
    if anagram != []:
        print()
        print(anagram)
    else:
        print("\nSorry, anagrams of", "'"+word+"'","could not be found.")
    file.close()