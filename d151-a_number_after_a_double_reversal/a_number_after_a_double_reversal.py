def isSameAfterReversals(num):
    return int(str((int(str(num)[::-1])))[::-1]) == num


print(isSameAfterReversals(123)) # True
print(isSameAfterReversals(1200)) # True
