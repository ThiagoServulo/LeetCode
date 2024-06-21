def summaryRanges(nums):
    # base case:
    if len(nums) == 0:
        return []
    # initialize result list:
    res = []
    # pointer to keep track of current range start:
    start = 0
    # iterate through nums:
    for i in range(0, len(nums)):
        # if i is at the end of the list or the current number is not equal to the next number - 1:
        if (i + 1) == len(nums) or nums[i] + 1 != nums[i + 1]:
            # add the current range to the result:
            res.append(str(nums[start]) if start == i else str(nums[start]) + "->" + str(nums[i]))
            # update start pointer:
            start = i + 1
    # return result:
    return res

print(summaryRanges([1,2,4,5,7]))