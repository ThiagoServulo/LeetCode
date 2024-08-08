def separateDigits(nums):
    ret = []
    for num in nums:
        ret.extend([int(n) for n in str(num)])
    return ret

print(separateDigits([13, 23])) # [1, 3, 2, 3]