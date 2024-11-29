def minElement(nums):
    return min(map(lambda x: sum([int(i) for i in str(x)]), nums))


print(minElement([999,19,199])) # 10