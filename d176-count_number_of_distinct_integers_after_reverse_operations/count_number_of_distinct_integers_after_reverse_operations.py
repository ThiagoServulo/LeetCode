def countDistinctIntegers(nums):
    aux1 = {str(n) for n in nums if len(str(n)) > 1}
    aux2 = {int(n[::-1]) for n in aux1}
    return len(aux2.union(set(nums)))

print(countDistinctIntegers([1,13,10,12,31])) # 6
print(countDistinctIntegers([2,2,2,2,])) # 1