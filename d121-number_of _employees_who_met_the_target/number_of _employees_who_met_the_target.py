def numberOfEmployeesWhoMetTarget(hours, target):
    return len([1 for h in hours if h >= target])

print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2)) # 3