# time conversion
# 22 March 2022

mm = {
    "01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July",
    "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"
}

hh = {
    "13": "1", "14": "2", "15": "3", "16": "4", "17": "5", "18": "6", "19": "7", "20": "8", "21": "9", "22": "10", "23": "11",
    "24": "00",
}

rank = {
    "1", "2", "3","21","22","23","31"
}

date = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

def post ():                            # returns position of the first -
    pos = date.index("-")
    pos = date.index("-", pos+1)
    pos = str(pos)
    return pos

pos = post()
pos = int(pos)
year = date[2:4]                        # returns last two numbers of the year

month = date.find("-")
month = date[month+1:month+3]
month = month.replace(month, mm[month]) # returns the month in full

day = int(date[pos+1:pos+3])            # finds the day
if day != rank:                         # adds the positional suffix
    if day == 1 or day == 31 or day == 21:
        day = str(day) 
        day = day+"st"
    elif day == 2 or day == 22:
        day = str(day) 
        day = day + "nd"
    elif day == 3 or day == 23:
        day = str(day) 
        day = day + "rd"
    else:
        day = str(day) 
        day = day + "th"

def hourr ():
    hour = date.find(":")
    hour = date[hour-2:hour]
    hour = int(hour)
    return hour

hour = hourr()
minu = date.find(":")
minu = date[minu:minu+3]                # finds the minutes in the time
if hour == 00:
    hour = "12" + minu + " "+ "am"
elif hour > 12 :                          # sets the am or pm of the time
    hour = str(hour)
    hour = hour.replace(hour, hh[hour]) # replaces the time from military time to am/pm time
    if hour == "00":
        hour = hour + minu + " "+ "am"
    else:
        hour = hour + minu + " "+ "pm"
else:
    hour = int(hour)
    if hour == 0:
        hour = date.find(":")
        hour = date[hour-2:hour]
        hour = hour[1]+ "0" + minu + " " + "am"
    elif hour < 10:
        hour = date.find(":")
        hour = date[hour-2:hour]
        hour = hour[1] + minu + " " + "am"
    else:
        if hour == 12:
            hour = str(hour)
            hour = hour + minu + " " + "pm"
        else:
            hour = str(hour)
            hour = hour + minu + " " + "am"
           
print(hour + " on the " + day + " of " + month + " " + "'" + year)