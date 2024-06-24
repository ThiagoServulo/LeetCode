def numberOf1Bits(num):
   if (num == 0):
      return 0
   else:
      return (num % 2) + numberOf1Bits(int(num / 2))


print(numberOf1Bits(10))