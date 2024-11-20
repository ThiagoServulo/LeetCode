def largestOddNumber(num):
    while len(num) > 0:
        if(int((num[::-1])[0]) % 2 == 0):
            num = num[:len(num) - 1:]
        else:
            return num
    return "" 



print(largestOddNumber("1234")) # 123
print(largestOddNumber("35427")) # 35427
print(largestOddNumber("224")) # ""