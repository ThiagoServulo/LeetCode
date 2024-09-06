def findTheArrayConcVal(nums):
    ret = 0
    for i in range(int(len(nums) / 2)):
        ret += int(str(nums[i]) + str(nums[len(nums) - 1 - i]))
    if(len(nums) % 2 == 1):
        ret += nums[int(len(nums) / 2)]
    return ret

print(findTheArrayConcVal([1,3,5,8])) # 53
print(findTheArrayConcVal([1,3,10,5,8])) # 63