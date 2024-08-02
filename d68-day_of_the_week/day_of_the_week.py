from datetime import date

def dayOfTheWeek(day, month, year):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    index  = date(year, month, day). weekday()
    return days[index]

print(dayOfTheWeek(31, 8, 2019)) # 'Saturday'