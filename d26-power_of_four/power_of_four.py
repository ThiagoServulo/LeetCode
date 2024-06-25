def isPowerOfFour(num): #3
   if(num <= 0):
      return False
   elif(num == 1):
      return True
   else:
      return (num % 4) == 0 and isPowerOfFour(num / 4) # true | false


print(isPowerOfFour(16))