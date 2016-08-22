'''
You are given the following information, but you may prefer to do some research for yourself.

1、1 Jan 1900 was a Monday.
2、Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
3、A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
# -*- coding: utf-8 -*

def f():
    daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # dayOfWeek = [0, 1, 2, 3, 4, 5, 6]  # 星期几，0代表周日
    r = [-1] * (100 * 12 + 1)  # 存放100年间每个月的第一天星期几
    d1900_01 = 1
    r[0] = (365 + d1900_01) % 7  # 1901年1月1日星期几
    for year in range(1901, 2000 + 1):
        for month in range(1, 12 + 1):
            index = (year - 1901) * 12 + month
            daysOfThisMonth = daysOfMonth[month - 1]
            if month == 2 and isLeapYear(year):
                daysOfThisMonth += 1
            r[index] = (r[index - 1] + daysOfThisMonth) % 7
    
    print(sum(map(lambda i:1 if r[i] == 0 else 0, range(1200))))

def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

f()
