def splitNum(num):
    l_num = sorted([n for n in str(num)])
    return int(''.join(l_num[::2])) + int(''.join(l_num[1::2]))
    
print(splitNum(4235)) # 59
print(splitNum(687)) # 75
