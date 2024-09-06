from collections import Counter

def isPossibleToSplit(nums):
    c = Counter(nums)
    for value in c.values():
        if value > 2:
            return False
    return True

print(isPossibleToSplit([1,1,2,2,3,4])) # True
print(isPossibleToSplit([1,1,1,1])) # False
