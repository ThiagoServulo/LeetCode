from collections import Counter

def maxFrequencyElements(nums):
    c = list(Counter(nums).values())
    return c.count(max(c)) * max(c)
        

print(maxFrequencyElements([1,2,2,3,1,4,5,5,5])) # 3