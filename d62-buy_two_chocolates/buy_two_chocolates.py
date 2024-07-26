def buyChoco(prices, money):
    min_1 = min(prices)
    for index in range(0, len(prices)):
        if prices[index] == min_1:
            prices.pop(index)
            break
    min_2 = min(prices)
    return (money - (min_1 + min_2)) if ((min_1 + min_2) <= money) else money


print(buyChoco([1,2,2], 3)) # 0
print(buyChoco([3,2,2], 3)) # 3