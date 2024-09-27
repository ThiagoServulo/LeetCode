def differenceOfSums(n, m):
    divisible = 0
    notDivisible = 0
    for i in range(0, n + 1):
        if(i % m) == 0:
            divisible += i
        else:
            notDivisible += i
    return notDivisible - divisible

print(differenceOfSums(5, 6)) # 15