def powerTwo(num): # 16
   if(num == 1):
      return True
   elif ((num % 2) != 0):
      return False
   else:
      return True and powerTwo(num / 2) # 8

print(powerTwo(17))