def subsets(nums): # [a,b,c]
   result = [[]]
   for n in nums:
      aux = []
      for subset in result:
         aux.append(subset + [n])
      result.extend(aux)
   return result

print(subsets([1,2,3]))