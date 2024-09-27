def subtractProductAndSum(n):
    produto = 1
    soma = 0
    for i in str(n):
        produto *= int(i)
        soma += int(i)
    return produto - soma

print(subtractProductAndSum(234)) # 15
print(subtractProductAndSum(4421)) # 21