def missingNumber(nums):
    nums.sort()
    for i in range(0, len(nums)):
        if i not in nums:
            return i
    return max(nums) + 1

print(missingNumber([3,0,1])) # 2
print(missingNumber([0,1])) # 2
print(missingNumber([9,6,4,2,3,5,7,0,1])) # 8