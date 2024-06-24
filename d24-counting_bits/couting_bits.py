def countBits(num):
    def decimaltobin(num):
        if(num == 1):
            return 1
        else:
            return (num % 2) + 10 * decimaltobin(int(num / 2))
    result = [0]
    for n in range(1, num + 1):
        result.append(str(decimaltobin(n)).count('1'))
    return result

print(countBits(5))