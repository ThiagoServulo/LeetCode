def alternateDigitSum(n):
    res = aux = 0
    for x in str(n):
        res = res + int(x) if (aux := aux + 1) % 2 else res - int(x)
    return res

print(alternateDigitSum(521)) # 4