#1 Jan 1900 was a Monday.
#Thirty days has September, April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


date_beg = [1,1,1901]
date_end = [12,31,2000]
month_day =[31,28,31,30,31,30,31,31,30,31,30,31]
month_day_l =[31,29,31,30,31,30,31,31,30,31,30,31]

### First what is the day of 1,1,1901

### to do so we need comparsion operation between two dates
def subtract_date(a_date1, a_date2):
    return [a_date1[0] - a_date2[0],a_date1[1] - a_date2[1],a_date1[2] - a_date2[2]]

def number_of_days_from_start(a_date1):
    month_day =[31,28,31,30,31,30,31,31,30,31,30,31]
    month_day_l =[31,29,31,30,31,30,31,31,30,31,30,31]
    start = [1,1,1900]
    diff = subtract_date(a_date1,start)
    days = 0
    while diff[2] != 0:
        if((start[2] % 4 == 0 and start[2] % 100 != 0) or start[2] % 400 == 0):
            days = days + sum(month_day_l)
        else:
            days = days + sum(month_day)
        start[2] = start[2] + 1
        diff[2] = diff[2] - 1
        
    if((start[2] % 4 == 0 and start[2] % 100 != 0) or start[2] % 400 == 0):
        days = days + sum(month_day_l[0:diff[0]]) + diff[1]
    else:
        days = days + sum(month_day[0:diff[0]]) + diff[1]    
    return days

def is_day_sunday(start_date, end_date):
    count = 0
    while number_of_days_from_start(start_date) < number_of_days_from_start(end_date):
        if number_of_days_from_start(start_date) % 7 == 6:
            count = count + 1
        start_date[0] = start_date[0] + 1
        if start_date[0] > 12:
            start_date[0] = 1
            start_date[2] = start_date[2] + 1
    return count
