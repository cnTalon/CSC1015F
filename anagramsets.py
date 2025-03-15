# anagram sets from wordlist
# 10 May 2022

import sys
sys.setrecursionlimit(30000)

wordList = []

file = open("EnglishWords.txt", "r")
print("***** Anagram Set Search *****")
length = eval(input("Enter word length:\n"))
filename = input("Enter file name:\n")
try:
    newFile = open(filename, "x")
except FileExistsError as eerno:    # if file exists we just rewrite
    newFile = open(filename, 'r+')
    newFile.truncate(0)             # empty file

def frequency(word):        # counts frequency of letters in word
    splitWord = {}
    for letter in set(word):
        splitWord[letter] = word.count(letter)
    return splitWord

for line in file:
    if "START" in line:     # finds start of wordlist
        for line in file:
            line = line[:-1]    # removes \n char
            if len(line) == length:     # checks if length meets input length
                wordList.append(line)   # forms wordlist with correct length words
wordList.sort()

def recur_ana(wordList):        # goes through each word and finding anagrams
    with open(filename, 'r+') as f:
        lst = f.readlines()
        if wordList == []:      # base case
            return
        else:
            wordbox = []
            word = wordList[0]      # selects first word in array to start comparing
            for words in wordList:
                if word != words and (frequency(word) == frequency(words)):
                    wordbox.append(word)
                    wordbox.append(words)
                    wordboxNew = set(wordbox)
                    wordboxNew = list(wordboxNew)
                    wordboxNew.sort()
                    if len(wordboxNew) > 2:
                        string = "['"+wordboxNew[0]+"', '"+wordboxNew[1]+"', '"+wordboxNew[2]+"']\n"
                    else:
                        string = "['"+wordboxNew[0]+"', '"+wordboxNew[1]+"']\n"
                    lst.insert(-1, string)
                    lst.sort()
                    with open(filename, 'w') as f:
                        f.writelines(lst)
            return recur_ana(wordList[1:])

print("Writing results...")
recur_ana(wordList)
file.close()