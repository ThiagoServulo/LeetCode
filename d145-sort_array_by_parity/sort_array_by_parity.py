def sortArrayByParity(nums):
    p = [n for n in nums if n % 2 == 0]
    p.sort(reverse=True)
    i = [n for n in nums if n % 2 != 0]
    i.sort(reverse=True)
    return p + i

print(sortArrayByParity([1,2,3,4]))