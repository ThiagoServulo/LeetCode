def dayOfYear(date):
    l_date = date.split('-')
    year = int(l_date[0])
    month = int(l_date[1])
    day = int(l_date[2])
    days_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 100 == 0):
        if (year % 400 == 0):
            days_months[1] = 29
    elif (year % 4 == 0):
        days_months[1] = 29
    return day + sum([days_months[x] for x in range(0, month - 1)])

print(dayOfYear("2019-02-10")) # 41
print(dayOfYear("1900-05-02")) # 122
