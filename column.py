# printing every 7th number
# 3 March 2022

n = eval(input("Enter a number: \n"))

if n > -6 and n < 2:
    for n in range(n, n+41, 7): 
            if n >= 0 and n <= 9:
                print("", n)
            else:
                print(n)
else:
    print("Enter a valid number.")