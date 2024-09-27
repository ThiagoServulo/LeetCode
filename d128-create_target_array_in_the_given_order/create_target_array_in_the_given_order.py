def createTargetArray(nums, index):
    res = []
    for n, i in zip(nums, index):
        res.insert(i, n)
    return res

print(createTargetArray([0,1,2,3,4], [0,1,2,2,1])) # [0, 4, 1, 3, 2]