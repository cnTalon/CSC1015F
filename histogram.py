# making a histogram of results
# 21 April 2022

nums = input("Enter a space-separated list of marks:\n")
nums = nums.split()     # separates the inputs into a list

# containers for the percentage brackets
first = []
upper2 =[]
lower2 = []
third = []
fail = []

# checks the inputs & sorts them into their brackets
for numbers in nums:
    if int(numbers) >= 75:
        first.append(numbers)
    elif int(numbers) >= 70 and int(numbers) <75:
        upper2.append(numbers)
    elif int(numbers) >= 60 and int(numbers) < 70:
        lower2.append(numbers)
    elif int(numbers) >= 50 and int(numbers) <60:
        third.append(numbers)
    else:
        fail.append(numbers)

# axes & prints an X for the number of marks in the particular bracket
print("1 |" + "X"*len(first))
print("2+|" + "X"*len(upper2))
print("2-|" + "X"*len(lower2))
print("3 |" + "X"*len(third))
print("F |" + "X"*len(fail))