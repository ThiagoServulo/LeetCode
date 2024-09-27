def numberOfSteps(num):
    aux = 0
    while num > 0:
        num = num - 1 if num % 2 else num / 2
        aux += 1
    return aux

print(numberOfSteps(123)) # 12