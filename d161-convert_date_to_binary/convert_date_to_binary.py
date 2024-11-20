def convertDateToBinary(date):
    def intToBin(num):
        num = int(num) if num is not int else num
        if num == 0:
            return 0
        return num % 2 + 10 * intToBin(int(num/2))
    date = date.split('-')
    return '-'.join(str(d) for d in map(intToBin, date))


print(convertDateToBinary("1900-01-01")) # "11101101100-1-1"