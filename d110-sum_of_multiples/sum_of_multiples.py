def sumOfMultiples(n):
    return sum([i for i in range(1, n + 1) if ((i % 3) == 0 or (i % 5) == 0 or (i % 7) == 0)])

print(sumOfMultiples(7)) # 21
print(sumOfMultiples(10)) # 40