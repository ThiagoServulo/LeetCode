def sumOfTheDigitsOfHarshadNumber(x):
    n = sum([int(i) for i in str(x)])
    return n if x % n == 0 else -1

print(sumOfTheDigitsOfHarshadNumber(18)) # 9
print(sumOfTheDigitsOfHarshadNumber(19)) # -1