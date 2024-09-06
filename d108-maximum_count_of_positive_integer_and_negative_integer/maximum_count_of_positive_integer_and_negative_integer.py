def maximumCount(nums):
    nums = list(filter(lambda x: x != 0, nums))
    pos = list(filter(lambda x: x >= 0, nums)).__len__()
    return max(pos, len(nums) - pos)

print(maximumCount([10,4,-2,0,0,3])) # 3
print(maximumCount([-2,-1,-1,1,2,3])) # 3
print(maximumCount([-1563,-236,-114,-55,427,447,687,752,1021,1636])) # 6