def sortArrayByParityII(nums):
    odds = [n for n in nums if n % 2 != 0]
    evens = [n for n in nums if n % 2 == 0]
    res = []
    for i in range(len(nums)):
        res.append(evens.pop() if i % 2 == 0 else odds.pop())
    return res


print(sortArrayByParityII([4,2,5,7]))