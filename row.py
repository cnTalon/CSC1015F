# print sequence of numbers
# 3 March 2022

num = eval(input("Enter the start number:\n"))

if num > -6 and num < 93:
    for num in range(num, num+7):
        if num >= 0 and num <=9:
            print("", num, end=' ')
        else:
            print(num, end=' ')
else:
    print("Enter a valid number.")