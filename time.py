# validity of time
# 26 February 2022

hours = eval(input("Enter the hours:\n"))
mins = eval(input("Enter the minutes:\n"))
secs = eval(input("Enter the seconds:\n"))

if (hours >= 0 and hours <=23):
    if mins >= 0 and mins <=59:
        if secs >=0 and secs <=59:
            print("Your time is valid.")
        else:
            print('Your time is invalid.')
    else:
        print('Your time is invalid.')
else:
    print('Your time is invalid.')
