def findDuplicate(nums): # [0, 1, 2, 2, 1]
    min_index = len(nums) + 1
    for index in range(0, len(nums)):
        if nums[index:].count(nums[index]) == 1:
            continue
        else:
            aux_index = nums.index(nums[index], index + 1)
            if(aux_index < min_index):
                min_index = aux_index
    return nums[min_index] if min_index != len(nums) + 1 else -1


print(findDuplicate([2,1,3,5,3,2]))
