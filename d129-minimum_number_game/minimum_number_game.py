def numberGame(nums):
    res = []
    while len(nums) > 0:
        nums.remove(a := min(nums))
        nums.remove(b := min(nums))
        res.extend([b, a])
    return res

print(numberGame([5,4,2,3])) # [3,2,5,4]