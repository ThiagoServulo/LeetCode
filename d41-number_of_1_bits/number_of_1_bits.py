def hammingWeight(n):
    return 0 if (n == 0) else (n % 2) + hammingWeight(int(n/2))

print(hammingWeight(11))