def arrangeCoins(n): # 3
   line = 1
   count = 0
   while(line <= n):
      n -= line 
      line += 1
      count += 1
   return count

print(arrangeCoins(12))