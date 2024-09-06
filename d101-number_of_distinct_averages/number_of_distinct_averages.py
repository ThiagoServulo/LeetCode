from collections import deque

def distinctAverages(nums):
    nums.sort()
    d = deque(nums)
    avarages = set()
    while len(d) > 0:
        avarages.add((d.pop() + d.popleft()) / 2)
    return len(avarages)

print(distinctAverages([4,1,4,0,3,5])) # 2