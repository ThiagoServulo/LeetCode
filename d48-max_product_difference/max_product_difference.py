def maxProductDifference(nums):
    nums.sort()
    return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

print(maxProductDifference([5,6,2,7,4])) # 34
print(maxProductDifference([4,2,5,9,7,4,8])) # 64
