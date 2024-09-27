def leftRightDifference(nums):
    left = [sum([nums[i] for i in range(0, x)]) for x in range(len(nums))]
    right = [sum([nums[i] for i in range(len(nums) - 1, x, -1)]) for x in range(len(nums) - 1 , -1, -1)][::-1]
    return [abs(left[i] - right[i]) for i in range(len(nums))]

print(leftRightDifference([10,4,8,3])) # [15,1,11,22]
print(leftRightDifference([1])) # [0]