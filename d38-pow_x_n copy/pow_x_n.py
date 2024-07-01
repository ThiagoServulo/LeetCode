def myPow(x: float, n: int) -> float: # 2, -1
    if(n == 0):
        return 1

    if(abs(n) == 1):
        return x if (n > 0) else (1 / x)
    
    return (1 / x) * myPow(x, n + 1) if(n < 0) else x * myPow(x, n - 1)

print(myPow(2, 3))