# program trace utility
# 9 May 2022

print("***** Program Trace Utility *****")
filename = input("Enter the name of the program file: ")

file = open(filename , 'r+')
stuff = file.readlines()
first = stuff[0]            # gets first line

if first.strip("\n") == '"""DEBUG"""':      # contains trace statements
    print("Program contains trace statements")
    stuff.remove('"""DEBUG"""\n')
    file.seek(0)
    for index, line in enumerate(stuff):
        if line.startswith('    """DEBUG"""'):
            stuff.remove(line)              # remove lines with trace statement

    with open(filename, 'w') as file:
        file.writelines(stuff)              # writes the remaining lines to file
    print("Removing...Done")
else:                                       # adds trace statements
    stuff.insert(0,'"""DEBUG"""\n')         # adds """DEBUG"""
    file.seek(0)
    file.writelines(stuff)
    for index, line in enumerate(stuff):
        if line.startswith("def"):          # adds trace statements to every function
            pos = index
            lineSplit = []
            lineSplit = line.split()        # separates line
            start = line.find("def")+4
            if "(" in lineSplit[1]:         # if brackets next to word
                end = lineSplit[1].find("(") +4
            else:                           # gap between bracket & word
                end = line.find("(")-1
            func = line[start:end]          # gets function name
            string = '    """DEBUG""";print(\''+func+'\')\n'
            stuff.insert(pos+1, string)

    with open(filename, 'w') as file:
        file.writelines(stuff)              # write final to file
    print("Inserting...Done")
file.close()