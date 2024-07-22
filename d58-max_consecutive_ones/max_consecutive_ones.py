def findMaxConsecutiveOnes(nums):
    max_1 = 0
    aux = 0
    for i in range(0, len(nums)):
        if(nums[i] == 1):
            aux += 1
        else:
            max_1 = max(max_1, aux)
            aux =0
    return max(max_1, aux)

print(findMaxConsecutiveOnes([1,1,0,1,1,1])) # 3