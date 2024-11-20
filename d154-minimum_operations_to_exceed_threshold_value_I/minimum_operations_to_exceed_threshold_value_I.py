def minOperations(nums, k):
    return len(nums) - len([n for n in nums if n >= k])

print(minOperations([2,11,10,1,3], 10)) # 3