# calendar printer
# 2 April 2022

import math


def day_of_week(day, month, year):
    # calculates the start day of the month
    if month == "January" or month == 1 or month == "February" or month == 2:
        start_day = ((day + math.floor(((13*(month+13))/5)) + (year-1) + math.floor(((year-1)/4)) - math.floor(((year-1)/100)) + math.floor(((year-1)/400)))) % 7
        start_day = ((start_day+5)% 7)+1
    else:
        start_day = ((day + math.floor(13*(month+1)/5) + year + math.floor((year/4)) - math.floor((year/100)) + math.floor((year/400)))) % 7
        start_day = ((start_day+5)% 7)+1
    return start_day

def is_leap(year):
    # first half tests for not century year & if divisible by 4 ----- second half tests for century year & century year divided by 400 is leap
    if ((year % 4 == 0) and (year % 100 !=0)) or ((year % 400 == 0) and (year % 100 == 0)):
        return True
    return False

def month_num(month_name):
    # assigns a number to the month name
    month_name = month_name.title()
    months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10,
                 "November":11, "December":12}
    month_numb = months[month_name]
    return month_numb

def num_days_in(month_num, year):
    # determines the number of days in a specific month
    num_days = 0
    if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num== 10 or month_num==12:
        num_days = 31
    elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
        num_days = 30
    elif month_num == 2:
        if is_leap(year) == True:       # checks for leap years and assigns appropriate number of days
            num_days = 29
        else:
            num_days = 28
    return num_days

def num_weeks(month_num, year):
    # counts the number of weeks in a month
    week = 0
    for rows in range(1,num_days_in(month_num,year)+1):
        if day_of_week(rows, month_num, year) == 7:
            week += 1                               # counts the last day of each week & adds
    if not day_of_week (num_days_in(month_num, year), month_num, year) == 7:
        week +=1                                    # adds a week if the last day of the month is not sunday
    return week

def week(week_num, start_day, days_in_month):
    # returns a string of numbers that represents the week
    week_string = ''
    start = 7 * (week_num-1) - (start_day -2)      # the start position of the week
    end = week_num * 7 - (start_day-2)           # the end number of the week
   
    for string in range(start, end):
        if string>0:                                    # checks that no 0 or negative values
            if not string == days_in_month +1:          # add string to week string as long as it is not the end of the month
                if string < 10 and (not string == end -1 or not len(week_string)) <= 2:     # if string is single digit add a blank space before
                    week_string += " "
                week_string += str(string)              # adds string to week string
                if not string == end -1:
                    week_string += ' '                  # if string is not the last string of the week, add a space after string
            else:
                break                                   # ends if month is done
        else:                                           # return blank spaces to fill the gaps of invalid dates
            week_string += '   '
    return week_string

def main():
    # asks for input and prints calendar
    month = input("Enter month:\n")
    year = eval(input("Enter year:\n"))
    print(month.title())
    print("Mo Tu We Th Fr Sa Su", end='')
    month = month_num(month)
    for x in range(num_weeks(month,year)+1):        # total number of weeks
        print(week(x, day_of_week(1, month, year), num_days_in(month,year)))    # prints each week

if __name__=='__main__':
    main()