def smallerNumbersThanCurrent(nums):
    return [len([i for i in nums if i < n]) for n in nums]


print(smallerNumbersThanCurrent([8,1,2,2,3])) # [4,0,1,1,3]
print(smallerNumbersThanCurrent([8,8,8])) # [0,0,0]
