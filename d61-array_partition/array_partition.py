def arrayPairSum(nums):
    nums.sort()
    max_possible = 0
    for i in range(0, len(nums) - 1, 2):
        max_possible += min(nums[i:i +2])
    return max_possible

print(arrayPairSum([6,2,6,5,1,2])) # 9
print(arrayPairSum([1,4,3,2])) # 4