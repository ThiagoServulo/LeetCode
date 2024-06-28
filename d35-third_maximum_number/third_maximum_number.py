def thirdMaximumNumber(nums):
    set_nums = set(nums)
    list_nums = list(set_nums)
    list_nums.sort(reverse=True)
    return list_nums[2] if len(list_nums) >= 3 else list_nums[0]

print(thirdMaximumNumber([5,4,3,3,2,2,1]))