def isPrimer(num):
    count = 0
    for n in range(1, num + 1):
        if((num % n) == 0):
            count += 1
        if(count > 2):
            return False
    return True

def isUglyNumber(num):
    for n in range(num, 1, -1):
        if isPrimer(n):
            if((num % n)) == 0 and n not in (2,3,5):
                return False
    return True

print(isUglyNumber(6))