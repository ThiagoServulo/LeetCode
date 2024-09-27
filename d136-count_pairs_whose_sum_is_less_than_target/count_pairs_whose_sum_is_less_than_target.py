def countPairs(nums, target):
    res = 0
    for i in range(len(nums)):
        current = nums[i]
        for n in nums[i+1::]:
            res += 1 if (current + n) < target else 0
    return res

print(countPairs([-1,1,2,3,1], 2))
    