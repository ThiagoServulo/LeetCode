def sumBase(n, k):
    return 0 if (n == 0) else (n % k) + sumBase(int(n / k), k)

print(sumBase(34, 6))
print(sumBase(10, 10))