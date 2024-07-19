def getConcatenation(nums):
    nums.extend(nums)
    return nums

print(getConcatenation([1,2,1])) # [1, 2, 1, 1, 2, 1]
print(getConcatenation([1,3,2,1])) # [1, 3, 2, 1, 1, 3, 2, 1]