def sumOfUnique(nums):
    return sum([x for x in nums if nums.count(x) == 1])

print(sumOfUnique([1,2,5,2]))