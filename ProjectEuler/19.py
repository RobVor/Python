"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

import datetime

def GetDay(intDay):
    StartDate = datetime.date(1901,1,1)
    EndDate = datetime.date(2001,1,1)
    Ordinal_Start = StartDate.toordinal()
    Ordinal_End = EndDate.toordinal()
    Dayz = 0

    for i in range(Ordinal_Start,Ordinal_End):
        day = datetime.date.fromordinal(i)
        print(day, day.day, day.weekday(), day.strftime("%A"))
        if (day.weekday() == (intDay - 1)) and (day.day == 1):
            Dayz += 1

    return Dayz

print(GetDay(7))