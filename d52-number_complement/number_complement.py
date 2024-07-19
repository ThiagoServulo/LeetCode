def calcComplement(num):
    if num == 1:
        return 0
    return  (0 if (num % 2) else 1) + 10 * calcComplement(int(num / 2))

def binToDec(num):
    if num == 0:
        return 0
    return (num % 10) + 2 * binToDec(int(num / 10))

def findComplement(num):
    return binToDec(calcComplement(num))

print(findComplement(5)) # 2