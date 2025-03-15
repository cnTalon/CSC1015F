# simple bbs
# 14 March 2022

print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
sel = input("Enter your selection:\n")
msg = None

while sel != "X" or sel !="x":
    if sel == "E" or sel =="e":
        msg = input("Enter the message:\n")
    if sel =="V" or sel =="v":
        if msg != None:                                       # if msg empty relay ori
            print("The message is:", msg)
        else:
            ori = "The message is: no message yet"
            print(ori)
    if sel =="L" or sel =="l":                                           # file list
        print("List of files: 42.txt, 1015.txt")
    if sel=="D" or sel =="d":
        ent = input("Enter the filename:\n")
        if ent == "1015.txt":
            txt2 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
            print(txt2)
        if ent == "42.txt":
            txt1 = "The meaning of life is blah blah blah ..."
            txt2 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
            print(txt1)
        if ent != "42.txt" and ent != "1015.txt":            # if unstored file relay error
            error = "File not found"
            print(error)
    if sel == "x" or sel == "X":                           # print if input is X
        print("Goodbye!")
        break
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    sel = input("Enter your selection:\n")  