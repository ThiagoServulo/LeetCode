def minimumOperations(nums):
    return len([n for n in nums if n % 3 != 0]) 

print(minimumOperations([1,2,3,4])) # 3