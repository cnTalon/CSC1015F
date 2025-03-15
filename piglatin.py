# translate to pig latin and back
# 12 April 2022

def to_pig_latin(s):
    latinpig = []
    s = s.split()   # separate sentence into singluar words
    for word in s:
        letter = word[0]    # selects the first letter
        if letter in ('a', 'e', 'i', 'o' ,'u'): # checks if letter is vowel
            piglatin = word + 'way'    # add 'way' to word beginning with vowel
        else:
            vowelMinPos = len(word)
            for letters in word:
                if letters in ('a', 'e', 'i', 'o' ,'u'):    # checks for vowels
                    if word.find(letters) < vowelMinPos and not word.find(letters) == -1:     # checks if vowel is in valid position
                        vowelMinPos = word.find(letters) # finds position of the vowel
                pos = vowelMinPos
                prevowel = word[0:pos]   # sequence of consonants before vowel
                aftervowel = word[pos:]  # sequence of consonants after vowel
                piglatin = aftervowel + "a" + prevowel + "ay"
        latinpig.append(piglatin)   # adds each piglatin word to a list
    pigged =' '.join(latinpig)      # compiles list into a string
    return pigged

def to_english(s):
    translated =[]
    s = s.split()       # separates sentence into singular words
    for word in s:
        key = "way"
        remove = word.find("w") # finds position of w
        string = word[remove:]  # extracts everything including & after w
        if string == key:       # execute if extracted word equals key
            english = word[0:remove]    # word will be everything from the beginning of the input till before the w
        else:
            key = "ya"
            string = word[:2:-1]    # extracts the last 2 letters of the word
            end = word.find("ay")   # find the position of "ay" and set it as the end
            newword = word[:end]    # creates a new word with the extracted letters
            letterstore =[]
            for letters in newword:
                if letters in ('a', 'e', 'i', 'o' ,'u'): # checks for vowels
                    letterstore.append(letters)     # add vowels to list
                    letters = letterstore[-1]       # select the last vowel from the list
                    vowelfinder = newword.rfind(letters)    # chooses the right most vowel in the word
                    prefix = newword[vowelfinder+1:]    # gets the letters after the vowels
                    rest = newword[:vowelfinder]    # gets the letters before the vowel
                    english = prefix + rest
        translated.append(english)  # add the word to a list
    english = ' '.join(translated)  # compiles list into a string
    return english


