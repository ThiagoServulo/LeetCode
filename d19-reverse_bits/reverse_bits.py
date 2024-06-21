def reverseBits(n: int) -> int:
    def binToInt(n: int) -> int: 
        if(n == 0): 
            return 0
        else:
            return (n % 10) + 2*binToInt(int(n / 10))

    num = binToInt(n)
    return int(str(num)[::-1])

print(reverseBits(111000111))