def differenceOfSum(nums):
    sum1 = sum(nums)
    sum2 = 0
    for num in [str(x) for x in nums]:
        sum2 += sum([int(n) for n in num])
    return abs(sum1 - sum2)

print(differenceOfSum([1,2,3,4]))
print(differenceOfSum([1,15,6,3]))