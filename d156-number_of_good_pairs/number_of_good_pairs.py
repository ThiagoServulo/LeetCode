def numIdenticalPairs(nums):
    count = 0
    for i in range(len(nums)):
        count += nums[i+1:].count(nums[i])
    return count

print(numIdenticalPairs([1,2,3,1,1,3])) # 4
    

