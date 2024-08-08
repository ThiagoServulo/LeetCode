def findMaxK(nums):
    nums.sort()
    for n in nums:
        if -n in nums:
            return abs(n)
    return -1

print(findMaxK([-1,10,6,7,-7,1])) # 7
print(findMaxK([-1,10])) # -1